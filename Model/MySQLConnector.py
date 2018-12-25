from mysql.connector.connection import MySQLConnection
from mysql.connector import errorcode
from Model.config import config
import mysql.connector


class MySQLConnector:
    connection = None

    def __init__(self):
        try:
            self.connection = MySQLConnection(**config)
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
        self.cur.commit()

    def update(self, query):
        self.cur.execute(query)
        self.cur.commit()

    def delete(self, query):
        self.cur.execute(query)
        self.cur.commit()

    def __del__(self):
        self.cur.close()
        self.connection.close()
        print("Connection closed")


if __name__ == '__main__':
    cnx = MySQLConnector()

    cnx.query("SELECT * FROM alumnos")
    print(cnx.cur)

    for row in cnx.cur:
        print(row)

    del cnx
