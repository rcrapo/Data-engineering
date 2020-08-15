import configparser

config = configparser.ConfigParser()
config.read('dl.cfg')

#clear out old tables
drop_imm = '''
                DROP TABLE IF EXISTS immigration;
'''
drop_state = '''
                DROP TABLE IF EXISTS state_demo;
'''
drop_airport = '''
                DROP TABLE IF EXISTS us_airports;
'''
drop_us_temp = '''
                DROP TABLE IF EXISTS us_temp;
'''
drop_city = '''
                DROP TABLE IF EXISTS city;
'''

#create schemas for each table

create_imm = '''CREATE TABLE IF NOT EXISTS public.immigration (
                  cicid bigint,
                  i94_month float,
                  origin_country varchar,
                  i94_port varchar,
                  arrival_date date,
                  travel_method varchar,
                  i94_state varchar,
                  departure_date date,
                  age float,
                  purpose_of_stay varchar,
                  file_date_add date,
                  birth_year float,
                  file_add_dt date,
                  gender varchar,
                  airline varchar,
                  admission_number float,
                  flight_num varchar,
                  visatype varchar
                   ); '''

create_state = '''CREATE TABLE IF NOT EXISTS public.state_demo (
                    state_code varchar,
                    native_american bigint,
                    asian bigint,
                    aa_black bigint,
                    hispanic_latino bigint,
                    white bigint,
                    num_veterans bigint,
                    foreign_born bigint,
                    male_population bigint,
                    female_population bigint,
                    total_population bigint,
                    median_age float,
                    avg_household_size float
                    );    '''

create_airport = '''CREATE TABLE IF NOT EXISTS public.us_airports (
                      airport_id varchar,
                      name varchar,
                      type varchar,
                      elevation_ft integer,
                      city_id bigint,
                      latitude float8,
                      longitude float8
                      );'''

create_temp = '''CREATE TABLE IF NOT EXISTS public.us_temp (
                   temp_id integer,
                   city_id bigint,
                   month integer,
                   avg_temp float8
                   );'''

create_city = '''CREATE TABLE IF NOT EXISTS public.city (
                   city_id bigint,
                   city varchar,
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
COPY us_temp FROM {}
      iam_role {}
      FORMAT AS PARQUET""").format(config['S3_redshift']['us_temp'],
                            config['IAM_ROLE']['ARN'])

airports_copy = ("""
COPY us_airports FROM {}
             iam_role {}
             FORMAT AS PARQUET""").format(config['S3_redshift']['us_airports'],
                                   config['IAM_ROLE']['ARN'])

city_copy = ("""
COPY city FROM {}
             iam_role {}
             FORMAT AS PARQUET""").format(config['S3_redshift']['city'],
                                   config['IAM_ROLE']['ARN'])




#data transfer ckecks
imm_quality = '''SELECT COUNT(*) FROM immigration'''
demo_quality = '''SELECT COUNT(*) FROM state_demo'''
temp_quality = '''SELECT COUNT(*) FROM us_temp'''
airport_quality = '''SELECT COUNT(*) FROM us_airports'''
city_quality = '''SELECT COUNT(*) FROM city'''

#null data query checks
imm_null = '''SELECT COUNT(*) FROM immigration WHERE cicid = NULL'''
demo_null = '''SELECT COUNT(*) FROM state_demo WHERE state_code = NULL'''
temp_null = '''SELECT COUNT(*) FROM us_temp WHERE temp_id = NULL'''
airport_null = '''SELECT COUNT(*) FROM us_airports WHERE airport_id = NULL'''
city_null = '''SELECT COUNT(*) FROM city WHERE city_id = NULL'''



#drop tables
drop_t = [drop_imm, drop_state, drop_airport, drop_us_temp, drop_city]

#create tables
create_tables = [create_state, create_airport, create_temp, create_city, create_imm]

#load the data with copy
copy_queries = [state_demo_copy, temp_copy, airports_copy, city_copy, immigration_copy]

#complied queries for quality and null data check functions
quality_c = [imm_quality, demo_quality, temp_quality, airport_quality, city_quality]
null_c = [imm_null, demo_null, temp_null, airport_null, city_null]
