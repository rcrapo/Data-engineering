import configparser

config = configparser.ConfigParser()
config.read('dl.cfg')

create_imm = '''CREATE TABLE IF NOT EXISTS public.immigration (
                  cicid varchar int NOT NULL PRIMARY KEY
                  i94_month
                  origin_country varchar
                  i94_port varchar
                  arrival_date date
                  travel_method varchar
                  i94_state varchar
                  departure_date date
                  age int
                  purpose_of_stay varchar
                  file_date_add date
                  visa_post varchar
                  occupation varchar
                  birth_year int
                  file_add_dt date
                  gender varchar
                  ins_num int
                  airline varchar
                  admission_number int
                  flight_num varchar
                  visatype varchar
                   ); '''

create_state = '''CREATE TABLE IF NOT EXISTS public.state_demo (
                    state_code varchar NOT NULL PRIMARY KEY
                    american_indian integer
                    asian integer
                    black integer
                    hispanic_latino integer
                    white integer
                    male_population integer
                    female_population integer
                    num_veterans integer
                    foreign_born integer
                    total_population integer
                    median_age numeric
                    avg_household_size numeric
                    );    '''

create_airport = '''CREATE TABLE IF NOT EXISTS public.us_airports (
                      airport_id varchar NOT NULL PRIMARY KEY
                      name varchar
                      type varchar
                      elevation_ft integer
                      city_id integer
                      gps_code varchar
                      iata_code varchar
                      latitude numeric
                      longitude numeric
                      );'''

create_temp = '''CREATE TABLE IF NOT EXISTS public.temperature (
                   temp_id integer NOT NULL PRIMARY KEY
                   city_id integer
                   month integer
                   avg_temp numeric
                   );'''

create_city = '''CREATE TABLE IF NOT EXISTS public.city (
                   city_id integer NOT NULL PRIMARY KEY
                   city varchar
                   state_code varchar
                    );'''

#load the processed table data from the s3 bucket

immigration_copy = ("""
COPY immigration FROM {}
             iam_role {}
             FORMAT AS PARQUET""").format(config['S3_redshift']['immigration'],
                                   config['IAM_ROLE']['ARN'])

state_demo_copy = ("""
COPY state_demo FROM {}
            iam_role {}
            FORMAT AS PARQUET""").format(config['S3_redshift']['state_demo'],
                                  config['IAM_ROLE']['ARN'])

temp_copy = ("""
COPY temp FROM {}
      iam_role {}
      FORMAT AS PARQUET""").format(config['S3_redshift']['temp'],
                            config['IAM_ROLE']['ARN'])

airports_copy = ("""
COPY airports FROM {}
             iam_role {}
             FORMAT AS PARQUET""").format(config['S3_redshift']['airports'],
                                   config['IAM_ROLE']['ARN'])

city_copy = ("""
COPY city FROM {}
             iam_role {}
             FORMAT AS PARQUET""").format(config['S3_redshift']['city'],
                                   config['IAM_ROLE']['ARN'])




#data transfer ckecks
imm_quality = '''SELECT COUNT(*) FROM immigration'''
demo_quality = '''SELECT COUNT(*) FROM state_demo'''
temp_quality = '''SELECT COUNT(*) FROM temp'''
airport_quality = '''SELECT COUNT(*) FROM airports'''
city_quality = '''SELECT COUNT(*) FROM city'''

#null data query checks
imm_null = '''SELECT COUNT(*) FROM immigration WHERE cicid = NULL'''
demo_null = '''SELECT COUNT(*) FROM state_demo WHERE state_code = NULL'''
temp_null = '''SELECT COUNT(*) FROM temp WHERE temp_id = NULL'''
airport_null = '''SELECT COUNT(*) FROM airports WHERE airport_id = NULL'''
city_null = '''SELECT COUNT(*) FROM city WHERE city_id = NULL'''




#create tables
create_tables = [create_imm, create_state, create_airport, create_temp, create_city]

#load the data with copy
copy_queries = [immigration_copy, state_demo_copy, temp_copy, airports_copy, city_copy]

#complied queries for quality and null data check functions
quality_check = [imm_quality, demo_quality, temp_quality, airport_quality, city_quality]
null_check = [imm_null, demo_null, temp_null, airport_null, city_null]
