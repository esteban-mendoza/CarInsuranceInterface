from mysql.connector.connection import MySQLConnection
from mysql.connector import errorcode
from Model.config import config
import mysql.connector


class MySQLConnector:

    def __init__(self):
        try:
            self.connection = MySQLConnection(**config)
            print("Connection created")

            self.cursor = None

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def create_cursor(self, dictionary=False):
        self.close_cursor()
        self.cursor = self.connection.cursor(dictionary=dictionary)

    def close_cursor(self):
        if self.cursor is not None:
            self.cursor.close()

    def query(self, query, args=None, dictionary=False):
        self.create_cursor(dictionary)
        if args is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, args)

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def insert(self, query):
        self.query(query)
        self.connection.commit()

    def update(self, query, args):
        self.query(query, args)
        self.connection.commit()

    def delete(self, query):
        self.query(query)
        self.connection.commit()

    def close(self):
        self.close_cursor()
        self.connection.close()
        print("Connection closed")


if __name__ == '__main__':
    # Example
    cnx = MySQLConnector()

    # cnx.query("SELECT * FROM cliente")
    # print(cnx.cursor)
    #
    # for row in cnx.cursor:
    #     print(row)

    cnx.query("create temporary table temp "
              "select * from "
              "cliente "
              "NATURAL JOIN poliza "
              "NATURAL JOIN factura "
              "NATURAL JOIN vehiculo")
    cnx.connection.commit()

    cnx.query("select * from temp")
    for row in cnx.cursor:
        print(row)

    cnx.close()
