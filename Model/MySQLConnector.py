from mysql.connector.connection import MySQLConnection
from mysql.connector import errorcode
import mysql.connector


class MySQLConnector:
    connection = None
    config = {
        'user': 'root',
        'password': 'password',
        'host': 'localhost',
        'database': 'fciencias'
    }

    def __init__(self):
        try:
            self.connection = MySQLConnection(**self.config)
            print("Connection created")

            self.cur = self.connection.cursor()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def query(self, query):
        self.cur.execute(query)

    def insert(self, query):
        self.cur.execute(query)

    def commit(self):
        self.cur.commit()

    def __del__(self):
        self.cur.close()
        self.connection.close()
        print("Connection closed")


if __name__ == '__main__':
    cnx = MySQLConnector()

    cnx.query("SELECT * FROM alumnos")

    for row in cnx.cur:
        print(row)

    del cnx
