import pyspark
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import udf, col
from pyspark.sql.types import *

import os
import configparser

from pyspark.sql.functions import year, month, avg
from pyspark.sql.window import Window as W

#creating the config object and reading the cfg file
config = configparser.ConfigParser()
config.read('dl.cfg')

#Accessing the AWS user IAM credentials located in the dl.cfg file using config object
os.environ['AWS_ACCESS_KEY_ID']=config.get('CREDENTIALS','AWS_ACCESS_KEY_ID')
os.environ['AWS_SECRET_ACCESS_KEY']=config.get('CREDENTIALS','AWS_SECRET_ACCESS_KEY')

spark = SparkSession.builder.appName('immigration').getOrCreate()

#function to extract the state cod from region field
region_to_state =  udf(lambda x:x.split('-')[-1])

#longitude and latitude functions
lat = udf(lambda x: x.split(", ")[0])
long = udf(lambda x: x.split(", ")[1])

def airport_process(input_data, output_data, spark):
    air = spark.read.format('csv').load(os.path.join(input_data, 'airports/airport-codes_csv.csv'),
                                        header=True, inferSchema=True)

    #filter down to us airports
    us_air = air.filter(air.iso_country =='US')

    us_air = us_air.select('ident',
                           'type',
                           'name',
                           'elevation_ft',
                           'iso_region',
                           'municipality',
                           'gps_code',
                           'iata_code',
                           'coordinates').withColumnRenamed('municipality', 'city')


    us_air = us_air.withColumn('state_code', region_to_state(col('iso_region')))

    #read in city table
    city = spark.read.parquet(os.path.join(output_data, "city/*"))

    us_air = us_air.join(city, (us_air.city==city.city) & (us_air.state_code==city.state_code), 'left')


    us_air = us_air.withColumn("latitude", lat("coordinates"))\
                   .withColumn("longitude", long("coordinates"))

    us_air = us_air.select('ident', 'name', 'type', 'elevation_ft',
                               'city_id', 'gps_code', 'iata_code', 'latitude', 'longitude')

    us_air = us_air.withColumnRenamed("ident", "airport_id")

    #us_air.write.partitionBy('type').mode('overwrite').parquet(os.path.join(output_data, "airports/"))
    us_air.write.mode('overwrite').csv(os.path.join(output_data, 'airports/'))
