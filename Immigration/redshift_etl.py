import psycopg2
import configparser
from sql_queries import drop_t, create_tables, copy_queries, quality_c, null_c

config = configparser.ConfigParser()
config.read('dl.cfg')

#drop tables to clear the path for new tables
def drop_tables(cur, conn):
    for query in drop_t:
        cur.execute(query)
        conn.commit()

#create schemas for redshift tables
def create_schemas(cur, conn):
    for query in create_tables:
        cur.execute(query)
        conn.commit()

#transfer processed parquet files to redshift cluster using COPY
def transfer_data(cur, conn):
    for query in copy_queries:
        cur.execute(query)
        conn.commit()

#run quality checks to see how many records exist in each redshift table
def quality_check(cur, conn):
    for query in quality_c:
        cur.execute(query)
        output = cur.fetchall()
        print("{} has {} records".format(query.split(' ')[-1], output[0][0]))
        conn.commit()

#check to see that there are no null values in primary key of redshift tables
def null_check(cur, conn):
    for query in null_c:
        cur.execute(query)
        output = cur.fetchall()
        print("{} has {} null values".format(query.split(' ')[3], output[0][0]))
        conn.commit()


def main():
    #read in config file
    config = configparser.ConfigParser()
    config.read('dl.cfg')

    #connect to redshift and instantiate cursor
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['REDSHIFT'].values()))
    cur = conn.cursor()

    #run each redshift etl function
    drop_tables(cur, conn)
    create_schemas(cur, conn)
    transfer_data(cur, conn)
    quality_check(cur, conn)
    null_check(cur, conn)

    conn.close()

if __name__ == "__main__":
    main()
