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

            self.cursor = self.connection.cursor()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def query(self, query):
        self.cursor.execute(query)

    def insert(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def update(self, query, args):
        self.cursor.execute(query, args)
        self.connection.commit()

    def delete(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
        print("Connection closed")


if __name__ == '__main__':
    cnx = MySQLConnector()

    cnx.query("SELECT * FROM alumnos")
    print(cnx.cursor)

    for row in cnx.cursor:
        print(row)

    # alumno = {
    #     'cuenta': 16,
    #     'nombre': 'Esteban',
    #     'id_carrera': 4
    # }
    # query = ("INSERT INTO ALUMNOS "
    #          "(cuenta, nombre, id_carrera) "
    #          "VALUES (%(cuenta)s, %(nombre)s, %(id_carrera)s)")
    #
    # cnx.insert(query, alumno)

    cnx.close()
