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

#register udf for parsing state code
region_state = udf(lambda x: x.split('-')[1])

spark = SparkSession.builder.appName('immigration').getOrCreate()

def city_process(input_data, output_data, spark):
    demo_df = spark.read.format('csv').load(os.path.join(input_data, 'demographics/*.csv'),
                                            header=True, inferSchema=True, sep=';')

    #cut down table and rename columns
    demo_df = demo_df.select('City','State Code')\
                     .withColumnRenamed('City', 'city')\
                     .withColumnRenamed('State Code', 'state_code')

    #read in airport data to get us cities
    df_air = spark.read.format('csv').load(os.path.join(input_data, 'airports/*.csv'),
                                           header=True, inferSchema=True)

    #filter down to only US cities
    us_air = df_air.filter(df_air.iso_country =='US')

    #apply function and rename municipality
    us_air = us_air.withColumn('state_code', region_state(col('iso_region')))\
                   .withColumnRenamed('municipality', 'city')\
                   .select('city', 'state_code')

    #combine the two dfs together to create the final city table
    city = us_air.union(demo_df)\
          .drop_duplicates()\
          .withColumn('city_Id', F.monotonically_increasing_id())\
          .withColumn('city_id,', F.row_number().over(W.orderBy('city_Id')))\
          .select('city_id', 'city', 'state_code')

    #write final df to s3 processed path
    city.write.mode('overwrite').parquet(os.path.join(output_data, 'city/'))
