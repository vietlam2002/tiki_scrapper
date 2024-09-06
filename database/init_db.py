import mysql.connector

from tikidb_config import read_db_config
from mysql.connector import MySQLConnection, Error

table_execute = ''

def db_init():
        conn = None
        try:
                db_config = read_db_config()
                conn = MySQLConnection(**db_config)
                if conn.is_connected():
                        print('connected to mysql database')
                        cursor = conn.cursor()
                        cursor.execute(table_execute)
                        print('created table')
        except Error as e:
                print(e)
        finally:
                if conn is not None and conn.is_connected():
                        conn.close()
                        print('connection closed')

if __name__ == '__main__':
        db_init()