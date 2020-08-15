import pyspark
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import udf, col
from pyspark.sql.types import *

from pyspark.sql.functions import year, month, avg
from pyspark.sql.window import Window as W

import os
import configparser

#creating the config object and reading the cfg file
config = configparser.ConfigParser()
config.read('dl.cfg')

#Accessing the AWS user IAM credentials located in the dl.cfg file using config object
os.environ['AWS_ACCESS_KEY_ID']=config.get('CREDENTIALS','AWS_ACCESS_KEY_ID')
os.environ['AWS_SECRET_ACCESS_KEY']=config.get('CREDENTIALS','AWS_SECRET_ACCESS_KEY')

spark = SparkSession.builder.appName('immigration').getOrCreate()

def temp_process(input_data, output_data, spark):
    '''
    This function contains all the functions and manipulations needed to shape and write the finished us_temp table
    Takes in the following parameters:

    input_data- the stem of the path for s3 bucket that you're pulling the data from
    output_data- the stem of the path for the finished data (where you're writing the data)
    spark- the spark session object to be used to read in the data
    '''

    #read in temp data
    temp = spark.read.format('csv').load(os.path.join(input_data, 'temperature/', 'GlobalLandTemperaturesByCity.csv'),
                                         header=True, inferSchema=True)
    #filter down to only US cities
    us_temp = temp.filter(temp.Country== 'United States')

    #create the 100 year boundaries
    lower_lim = F.to_date(F.lit("1912-01-01")).cast(TimestampType())
    upper_lim = F.to_date(F.lit("2011-12-31")).cast(TimestampType())

    #filter according to time boundaries
    us_temp = us_temp.filter((us_temp.dt >= lower_lim) & (us_temp.dt <= upper_lim))

    #drop null values
    us_temp = us_temp.na.drop()

    #extract the month and year in order to find the aggregate temperature
    us_temp = us_temp.withColumn('month', month(us_temp.dt)).withColumn('year', year(us_temp.dt))

    #modify latitude and longitude columns
    us_temp = us_temp.withColumn("latitude", F.split(us_temp['Latitude'], 'N')[0].cast(FloatType()))\
                     .withColumn('longitude', F.split(us_temp['Longitude'], 'W')[0].cast(FloatType())*-1)

    # average the temperature in each city by month across 100 years, rename columns, and
    us_temp = us_temp.groupBy('City', 'month')\
           .agg(F.round(avg('AverageTemperature'), 2).alias('avg_temp'),
                F.round(avg('AverageTemperatureUncertainty'),2).alias('avg_std'))\
           .orderBy('City','month')\
           .withColumn('temp_Id', F.monotonically_increasing_id())\
           .withColumn("temp_id", F.row_number().over(W.orderBy('temp_Id')))\
           .withColumnRenamed('City', 'city')\
           .select("temp_id","city", "month", "avg_temp")

    #read in city table
    city = spark.read.parquet(os.path.join(output_data, "city/*.parquet"))
    city.show(5)

    #join city table to temp table to insert city_id field
    us_temp = us_temp.join(city, us_temp.city==city.city, 'left')

    #get rid of duplicate values and shape final table
    us_temp = us_temp.drop_duplicates(subset=['city', 'month'])\
                     .select('temp_id','city_id', 'month', 'avg_temp')

    #display final data for intermediate quality check
    us_temp.count()
    us_temp.show(5)

    #write to parquet and store in us_imm bucket
    us_temp.write.mode('overwrite').parquet(os.path.join(output_data, 'us_temp/'))
