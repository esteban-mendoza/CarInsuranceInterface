from Model.MySQLConnector import MySQLConnector
from datetime import date, datetime, timedelta
import traceback
import logging


class Controller:

    def __init__(self):
        self.connection = MySQLConnector()

    def __del__(self):
        self.connection.close()

    @staticmethod
    def str_helper(data):
        fields = str()
        values = str()

        for field in data.keys():
            fields += "{}, ".format(field)

        for value in data.values():
            if type(value) is int or type(value) is float:
                values += "{}, ".format(value)
            else:
                values += "\'{}\', ".format(str(value))

        fields = fields.rstrip(", ")
        values = values.rstrip(", ")

        return fields, values

    def insert_cliente(self, **data):
        fields, values = self.str_helper(data)

        query = ("INSERT INTO cliente "
                 "(" + fields + ") "
                 "VALUES (" + values + ")")
        try:
            self.connection.insert(query)
        except Exception as e:
            logging.error(traceback.format_exc())

    def insert_vehiculo(self, **data):
        fields, values = self.str_helper(data)

        query = ("INSERT INTO vehiculo "
                 "(" + fields + ") "
                 "VALUES (" + values + ")")
        try:
            self.connection.insert(query)
        except Exception as e:
            logging.error(traceback.format_exc())

    def insert_factura(self, **data):
        fields, values = self.str_helper(data)

        query = ("INSERT INTO factura "
                 "(" + fields + ") "
                 "VALUES (" + values + ")")
        try:
            self.connection.insert(query)
            self.update_vehiculo(data['placas'])
        except Exception as e:
            logging.error(traceback.format_exc())

    def update_vehiculo(self, placas):
        query = ("SELECT id_factura FROM factura "
                 "WHERE placas=\"{}\"".format(placas))

        self.connection.query(query)

        update_statement = ("UPDATE vehiculo "
                            "SET id_factura = %s "
                            "WHERE placas = %s")

        for id_factura in self.connection.cursor:
            self.connection.update(update_statement, (id_factura[0], placas))
