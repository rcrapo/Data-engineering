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

#import functions from scripts for etl
from city import city_process
from airports import airport_process
from state_demo import demo_process
from temp import temp_process
from immigration import imm_process


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

#function to extract the state cod from region field
region_to_state =  udf(lambda x:x.split('-')[-1])

#longitude and latitude functions
lat = udf(lambda x: x.split(", ")[0])
long = udf(lambda x: x.split(", ")[1])

#UDFS for immigration etl
admission_date = udf(lambda x: str_todate_A(x), DateType())
file_date = udf(lambda x: str_todate_F(x), DateType())
sas_date = udf(lambda x: unix_convert(x), DateType())


#bucket access
input_data = config.get('S3', 'input_data')
output_data = config.get('S3', 'output_data')



def main():

    #configure spark to read sas data files
    spark = SparkSession.builder\
                        .config("spark.jars.packages","saurfang:spark-sas7bdat:2.0.0-s_2.11")\
                        .enableHiveSupport().getOrCreate()

    input_data = 's3://us-imm/us-imm/raw/'
    output_data = 's3://us-imm/us-imm/lake/'
    #run each function
    city_process(input_data, output_data, spark)
    demo_process(input_data, output_data, spark)
    temp_process(input_data, output_data, spark)
    airport_process(input_data, output_data, spark)

    #need to figure out why 'immigration' module won't import
    #imm_process(input_data, output_data, spark)

    #stop session
    spark.stop()

if __name__ == "__main__":
    main()
