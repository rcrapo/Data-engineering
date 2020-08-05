import psycopg2
import configparser
from sql_queries import create_tables, copy_queries, quality_check, null_check

config = configparser.ConfigParser()
config.read('dl.cfg')

def create_schemas(cur, conn):
    for query in create_tables:
        cur.execute(query)
        conn.commit()

def transfer_data(cur, conn):
    for query in copy_queries:
        cur.execute(query)
        conn.commit()

def quality(cur, conn):
    for query in quality_check:
        cur.execute(query)
        output = cur.fetchall()
        print("{} has {} records".format(query.split(' ')[-1], output))
        conn.commit()

def null_check(cur, conn):
    for query in null_check:
        cur.execute(query)
        output = cur.fetchall()
        print("{} has {} null values".format(query.split(' ')[3], output))
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dl.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    create_schemas(cur, conn)
    transfer_data(cur, conn)
    quality(cur, conn)
    null_check(cur, conn)

    conn.close()

if __name__ == "__main__":
    main()
