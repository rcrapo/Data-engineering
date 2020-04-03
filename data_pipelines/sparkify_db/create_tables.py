import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

#drops all tables if there are any in the redshift cluster
def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

#creates the structure for all tables in the redshift cluster
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

#ties all functions and queries together for all table creations
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
