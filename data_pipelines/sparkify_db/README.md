# Purpose of Database

This database was designed with the goal of understading the behaviour of Sparkify's users (simulated data). At the core of this database is the songplays table that contains information about which songs were played by who and at what time. The other tables provide further qualitative information that can help anlysts flesh out the finer details of how sparkify is doing and where it can grow. The information in this database will help sparkify in the following ways:

1. Understanding this type of data will help sparkify grow as they can identify certain music artists that are popular. This will inform stakeholders in the song curation process to know which artists to seek out in building the song database.
2. Understanding user demographics can help guide marketing and advertising campaigns. For instance, if sparkify discovers that women between the ages of 20 and 35 listen to sparkify mostly in the early dawn or post 5pm, stakeholders could surmise that sparkify is often used as a workout companion. This may lead to marketing campaigns or promotions with wireless ear bud brands, water bottle brands, fitness gear etc.
3. In addition to effectiveness, understanging the user demographics can help save the company money in ad spending. Understanding the locations of the users and the browser info can help deploy ad acampaigns with precision.

# Design Schema

The database follows the star schema design with the songplays fact table at the center and the users, songs, artists and time dimension tables as the points of the star. This database has been pulled from song and log data from the udacity-dend s3 bucket. This data has then been loaded into Amazon Redshift and designed intuitively for easy querying or app analytics. 

Additionally, the staging tables, which contain the data in its original form, are also placed into redshift. The star schema provides easy access for BI analysts, but having the original tables available in redshift can give greater flexibility to any ML engineers or data scientists.

## Scripts

The **sql_queries.py** script contains all the queries that create the structure for all the intermediate and final tables that are housed in Redshift. 

The **etl.py** script pulls the data from the s3 bucket using the copy function and inserts the respective log and song data into staging tables. From here the data for the fact and dimension tables are pulled from the staging tables and shaped through transformations, joins and slicing in order to fit the structure of the final tables.

# Instructions

1) Make sure that the dwh.cfg file has the proper credentials needed to connect to an up and running redshift cluster (one that you have set up).
2) Open a terminal and type "python create_tables.py" and hit enter to connect to the redshift cluster of your choosing and build the table schemas.
3) After the create_tables.py runs, type in "python etl.py" and hit enter. This then takes the data from the already filled s3 bucket and transforms and loads the data into your redshift tables. You can now query the database inside the redshift cluster for any intel you need.
