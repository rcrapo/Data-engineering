import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP table IF EXISTS staging_events"
staging_songs_table_drop = "DROP table IF EXISTS staging_songs"
songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES
#creating the staging tables
staging_events_table_create= ("""
CREATE table staging_events 
(artist text, 
 auth text, 
 firstName text, 
 gender text,
 itemInsession int,
 lastName text,
 length numeric,
 level text,
 location text,
 method text,
 page text,
 registration numeric,
 sessionId int,
 song text,
 status int,
 ts bigint,
 userAgent text,
 userId int)
""")

staging_songs_table_create = ("""
CREATE table staging_songs
(artist_id text,
 artist_latitude numeric,
 artist_location text,
 artist_longitude text,
 artist_name text,
 duration numeric,
 num_songs int,
 song_id text,
 title text,
 year int)
""")

#creating the the tables using a star schema design
#fact table: songplays
#dimension tables: user, songs, artists, time

songplay_table_create = ("""
CREATE table songplays 
(songplay_id int IDENTITY(0,1) PRIMARY KEY, 
start_time timestamp NOT NULL, 
user_id integer NOT NULL, 
level text, 
song_id text, 
artist_id text, 
session_id integer, 
location text, 
user_agent text)
""")

user_table_create = ("""
CREATE table users 
(user_id integer NOT NULL PRIMARY KEY, 
first_name text, 
last_name text, 
gender text, 
level text)
""")

song_table_create = ("""
CREATE table songs 
(song_id text PRIMARY KEY NOT NULL, 
title text, 
artist_id text NOT NULL, 
year integer, 
duration integer)
""")

artist_table_create = ("""
CREATE table artists 
(artist_id text NOT NULL PRIMARY KEY, 
name text, 
location text, 
latitude numeric, 
longitude numeric)
""")

time_table_create = ("""CREATE table time 
(start_time timestamp NOT NULL PRIMARY KEY, 
hour integer, 
day integer, 
week integer, 
month integer, 
year integer, 
weekday text)
""")

# STAGING TABLES
# transfering the data from the s3 bucket into staging tables created in redshift
# make sure that you have the proper credentials filled out for each variable in the dwh.cfg file

staging_events_copy = ("""
COPY staging_events FROM {} 
                    iam_role {} 
                    json {}""").format(config['S3']['LOG_DATA'], config['IAM_ROLE']['ARN'], config['S3']['LOG_JSONPATH'])

staging_songs_copy = ("""
COPY staging_songs FROM {}
                iam_role {} 
                json 'auto'""").format(config['S3']['SONG_DATA'], config['IAM_ROLE']['ARN'])

# FINAL TABLES

#inserting the data from the staging tables into the final tables

#NOTE the songplay insert query changes the datatype of ts (staging_events) from bigint into timestamp
songplay_table_insert = ("""
INSERT into songplays 
(start_time, user_id, 
level, song_id, 
artist_id, session_id, 
location, user_agent) 
SELECT se.start_time,
       se.userId as userId,
       se.level as level,
       ss.song_id as song_id,
       ss.artist_id as artist_id,
       se.sessionId as sessionId,
       se.location as location,
       se.userAgent as userAgent
FROM (SELECT TIMESTAMP 'epoch' + ts/1000 * interval '1 second' AS start_time, * 
FROM staging_events
WHERE page='NextSong') se
LEFT JOIN staging_songs ss
ON (se.song = ss.title)
AND (se.artist = ss.artist_name)
AND (se.length = ss.duration)
""")

user_table_insert = ("""
INSERT into users 
(user_id, first_name, 
last_name, gender, level)
SELECT DISTINCT userId,
        firstName,
        lastName,
        gender,
        level
FROM staging_events
WHERE page='NextSong'
""")

song_table_insert = ("""
INSERT into songs 
(song_id, title, 
artist_id, year, duration) 
SELECT DISTINCT song_id,
        title,
        artist_id,
        year,
        duration
FROM staging_songs
""")

artist_table_insert = ("""
INSERT into artists 
(artist_id, name, 
location, latitude, longitude) 
SELECT artist_id,
       artist_name,
       artist_location,
       artist_latitude,
       artist_longitude
FROM staging_songs
""")

time_table_insert = ("""INSERT into time 
(start_time, hour, day, 
week, month, year, weekday)
SELECT DISTINCT start_time, 
EXTRACT(HOUR FROM start_time) as hour,
EXTRACT(DAY FROM start_time) as day,
EXTRACT(WEEK FROM start_time) as week,
EXTRACT(MONTH FROM start_time) as month,
EXTRACT(YEAR FROM start_time) as year,
EXTRACT(dayofweek FROM start_time) as weekday
FROM songplays
""")

# QUERY LISTS

# queries are compiled into lists to be used in the create_tables.py and etl.py scripts

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
