import os
import psycopg2
import psycopg2.pool
import psycopg2.extras
import logging
import time

conn_string = os.environ.get('PGCONN')

# Set a sensible default if no connection provided
if conn_string is None:
    conn_string = "host=db dbname=cmapper port=5432 user=cmapper password=cmapper"

while True:
    try:
        conn_pool = psycopg2.pool.ThreadedConnectionPool(1, 20, conn_string)
        break
    except (Exception, psycopg2.OperationalError) as error:
        logging.error("Error trying to connect threaded connection pool: {}".format(error))
        logging.error("Sleeping 10s to wait for postgresql to come up...")
        time.sleep(10)


def _get_cursor(conn):
    return conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


def mutate(sql, args):
    """
    Use for running mutations (INSERT, UPDATE, DELETE)
    :param sql: A string containing the mutation or the name of the stored procedure/function
    :param args: any parameters that need to be inserted into the string
    :return: ID of record just inserted or -1
    """
    result = -1
    try:
        with conn_pool.getconn() as conn, _get_cursor(conn) as cursor:
            logging.debug("Querying with {} and {}".format(sql, args))
            cursor.execute(sql, args)
            result = cursor.fetchone()
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as dberror:
        logging.error("Mutation error: {}".format(dberror))
        logging.error("Mutation error sql: {} - args: {}".format(sql, args))
    finally:
        conn_pool.putconn(conn)
        return result


def query(sql, args):
    """
    Use for running SELECT queries
    :param sql: A string containing the query or the name of the stored procedure/function
    :param args: any parameters that need to be inserted into the string
    :return: list of dicts (records) or None
    """
    records = None
    try:
        with conn_pool.getconn() as conn, _get_cursor(conn) as cursor:
            logging.debug("Querying with {} and {}".format(sql, args))
            cursor.execute(sql, args)
            records = cursor.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error("Query error: {}".format(error))
        logging.error("Query error sql: {} - args: {}".format(sql, args))
    finally:
        conn_pool.putconn(conn)

    return records
