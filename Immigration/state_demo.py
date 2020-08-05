import pyspark
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import udf, col
from pyspark.sql.types import *

import os
import configparser

spark = SparkSession.builder.appName('immigration').getOrCreate()

#creating the config object and reading the cfg file
config = configparser.ConfigParser()
config.read('dl.cfg')

#Accessing the AWS user IAM credentials located in the dl.cfg file using config object
os.environ['AWS_ACCESS_KEY_ID']=config.get('CREDENTIALS','AWS_ACCESS_KEY_ID')
os.environ['AWS_SECRET_ACCESS_KEY']=config.get('CREDENTIALS','AWS_SECRET_ACCESS_KEY')


def demo_process(input_data, output_data, spark):

    state_demo = spark.read.format('csv').load(os.path.join(input_data, 'demographics/','us-cities-demographics.csv'),
                                               header=True, inferSchema=True, sep=';')

    race_demo = state_demo.select('City', 'State Code', 'Race', 'Count')

    race_demo = race_demo.groupby('State Code').pivot('Race').sum('Count')

    race_demo = race_demo.withColumnRenamed('American Indian and Alaska Native', 'native_american')\
                         .withColumnRenamed('Asian', 'asian')\
                         .withColumnRenamed('Black or African-American', 'aa_black')\
                         .withColumnRenamed('Hispanic or Latino', 'hispanic_latino')\
                         .withColumnRenamed('White', 'white')

    state_demo = state_demo.select('State Code', 'Median Age',
                                       'Male Population', 'Female Population',
                                       'Total Population', 'Number of Veterans',
                                       'Foreign-born', 'Average Household Size')

    state_demo = state_demo.groupby('State Code').agg(F.mean('Median Age').alias('med_age'),
                                         F.sum('Male Population').alias('male_population'),
                                         F.sum('Female Population').alias('female_population'),
                                         F.sum('Total Population').alias('total_population'),
                                         F.sum('Number of Veterans').alias('num_of_veterans'),
                                         F.sum('Foreign-born').alias('foreign_born'),
                                         F.mean('Average Household Size').alias('avg_household_sz'))

    state_demo = state_demo.withColumn('median_age', F.round(state_demo['med_age'], 2))\
                           .withColumn('avg_household_size', F.round(state_demo['avg_household_sz'], 2))

    state_demo = state_demo.withColumnRenamed('State Code', 'state_code')\
                           .drop('med_age', 'avg_household_sz')

    state_demo = state_demo.join(race_demo, state_demo['state_code']==race_demo['State Code'], 'left')

    state_demo = state_demo.drop("State Code")

    #write to parquet and store in us_immigration bucket

    #state_demo.write.mode('overwrite').parquet(os.path.join(output_data, 'state_demographics/'))
    state_demo.write.mode('overwrite').csv(os.path.join(output_data, 'state_demographics/'))
