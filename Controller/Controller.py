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

    def gen_poliza(self, **data):
        costo_factura = self.get_costo_factura(data['id_factura'])

        prima = costo_factura * 0.85
        data['prima_asegurada'] = data.get('prima_asegurada', prima)

        costo_seguro = costo_factura * (6.67/12)/100
        data['costo_total'] = data.get('costo_total', costo_seguro)

        fecha_apertura = date.today().strftime("%Y-%m-%d")
        data['fecha_apertura'] = data.get('fecha_apertura', fecha_apertura)

        fecha_vencimiento = datetime.strptime(data['fecha_apertura'], "%Y-%m-%d") + timedelta(days=365)
        fecha_vencimiento = fecha_vencimiento.strftime("%Y-%m-%d")
        data['fecha_vencimiento'] = data.get('fecha_vencimiento', fecha_vencimiento)

        fields, values = self.str_helper(data)

        query = ("INSERT INTO poliza "
                 "(" + fields + ") "
                 "VALUES (" + values + ")")
        try:
            self.connection.insert(query)
        except Exception as e:
            logging.error(traceback.format_exc())



    def get_costo_factura(self, id_factura):
        query = ("SELECT costo_total FROM factura "
                 "WHERE id_factura = %s")

        self.connection.query(query, (id_factura,))

        return self.connection.cursor.fetchone()[0]
