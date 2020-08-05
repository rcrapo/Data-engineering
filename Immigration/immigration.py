import pyspark
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import udf, col
from pyspark.sql.types import *

#import helpers
#from Helpers.Data_transform import Data_dictionary as DD
from Data_transform import Data_dictionary as DD

#any other needed python packages
import datetime
import os
import configparser

#creating the config object and reading the cfg file
config = configparser.ConfigParser()
config.read('dl.cfg')

#Accessing the AWS user IAM credentials located in the dl.cfg file using config object
os.environ['AWS_ACCESS_KEY_ID']=config.get('CREDENTIALS','AWS_ACCESS_KEY_ID')
os.environ['AWS_SECRET_ACCESS_KEY']=config.get('CREDENTIALS','AWS_SECRET_ACCESS_KEY')

#regular functions for immigration
def str_todate_A(x):
    try:
        return datetime.datetime.strptime(x, '%m%d%Y')
    except:
        return None

def str_todate_F(x):
    try:
        return datetime.datetime.strptime(x, '%Y%m%d')
    except:
        return None

def unix_convert(x):
    try:
        start = datetime.datetime(1960, 1, 1)
        return start + datetime.timedelta(days=int(x))
    except:
        return None


#UDFS for immigration etl
admission_date = udf(lambda x: str_todate_A(x), DateType())
file_date = udf(lambda x: str_todate_F(x), DateType())
sas_date = udf(lambda x: unix_convert(x), DateType())


#bucket access
input_data = config.get('S3', 'input_data')
output_data = config.get('S3', 'output_data')

#configure spark to read sas data files
spark = SparkSession.builder\
                    .config("spark.jars.packages","saurfang:spark-sas7bdat:2.0.0-s_2.11")\
                    .enableHiveSupport().getOrCreate()


def imm_process(input_data, output_data, spark):
    #load the june dataframe
    june = spark.read.format("com.github.saurfang.sas.spark")\
                     .load(os.path.join(input_data, "immigration/june/i94_jun16_sub.sas7bdat"),
                           header=True,inferSchema=True)

    #read in the other files
    imm_df = spark.read.format("com.github.saurfang.sas.spark")\
                        .load(os.path.join(input_data, "immigration/other/i94_apr16_sub.sas7bdat"),
                              header=True, inferSchema=True)

    #list columns that need to be used
    columns = ['cicid', 'i94mon', 'i94res','i94port','arrdate', 'i94mode','i94addr',
            'depdate','i94bir', 'i94visa', 'dtadfile', 'visapost', 'occup',
            'biryear', 'dtaddto', 'gender', 'insnum', 'airline', 'admnum', 'fltno','visatype']

    #combine the two dfs together
    imm_df = imm_df.select(columns).union(june.select(columns))\
                                   .withColumn('cicid', F.monotonically_increasing_id())

    #change column names with mapper
    imm_df = imm_df.select([col(c).alias(DD.data_dict['column_names'].get(c, c)) for c in imm_df.columns])

    #recast the data types for better management
    imm_df = imm_df.withColumn('arrival_date', imm_df.arrival_date.cast(IntegerType()))\
                   .withColumn('departure_date', imm_df.departure_date.cast(IntegerType()))\
                   .withColumn('file_date_add', imm_df.file_date_add.cast(StringType()))\
                   .withColumn('i94_residence', imm_df.i94_residence.cast(StringType()))\
                   .withColumn('travel_method', imm_df.travel_method.cast(StringType()))\
                   .withColumn('purpose_of_stay', imm_df.purpose_of_stay.cast(StringType()))

    #convert each date column to date type data
    imm_df = imm_df.withColumn('arrival_date', sas_date(col('arrival_date')))\
                   .withColumn('departure_date', sas_date(col('departure_date')))\
                   .withColumn('file_date_add', file_date(col('file_date_add')).cast(DateType()))\
                   .withColumn('admission_date', admission_date(col('admission_date')).cast(DateType()))

    #map more legible values to df
    imm_df = imm_df.replace(to_replace=DD.data_dict['purpose_of_stay'], subset=['purpose_of_stay'])
    imm_df = imm_df.replace(to_replace=DD.data_dict['travel_method'], subset=['travel_method'])
    imm_df = imm_df.replace(to_replace=DD.data_dict['cit_res'], subset=['i94_residence'])
    imm_df = imm_df.replace(to_replace=DD.data_dict['port'], subset=['i94_port'])

    #write the table to parquet file
    #imm_df.write.partitionBy('i94_month').mode('overwrite').parquet(os.path.join(output_data, "immigration/"))
    imm_df.write.mode('overwrite').csv(os.path.join(output_data, 'immigration/'))
