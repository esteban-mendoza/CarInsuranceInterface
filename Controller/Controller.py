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

    @staticmethod
    def where_helper(data):
        where_clause = str()

        for key, value in data.items():
            where_clause += "{}=\'{}\' AND ".format(key, value)

        where_clause = where_clause.rstrip(" AND ")

        return where_clause

    def insert_cliente(self, **data):
        fields, values = self.str_helper(data)

        query = ("INSERT INTO cliente "
                 "(" + fields + ") "
                 "VALUES (" + values + ")")
        try:
            self.connection.insert(query)
        except Exception as e:
            logging.error(traceback.format_exc())

    def search_cliente(self, **data):
        clauses = self.where_helper(data)

        query = ("SELECT * " 
                 "FROM cliente "
                 "WHERE " + clauses)

        self.connection.query(query, dictionary=True)
        return self.connection.fetchone()

    def insert_clientes(self, path):
        print(path)

    def insert_vehiculo(self, **data):
        fields, values = self.str_helper(data)

        query = ("INSERT INTO vehiculo "
                 "(" + fields + ") "
                 "VALUES (" + values + ")")
        try:
            self.connection.insert(query)
        except Exception as e:
            logging.error(traceback.format_exc())

    def search_vehiculo(self, **data):
        clauses = self.where_helper(data)

        query = ("SELECT * " 
                 "FROM vehiculo "
                 "WHERE " + clauses)

        self.connection.query(query, dictionary=True)
        return self.connection.fetchone()

    def insert_vehiculos(self, path):
        print(path)

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

    def search_factura(self, **data):
        clauses = self.where_helper(data)

        query = ("SELECT * " 
                 "FROM factura "
                 "WHERE " + clauses)

        self.connection.query(query, dictionary=True)
        return self.connection.fetchone()

    def insert_facturas(self, path):
        pass

    def update_vehiculo(self, placas):
        query = ("SELECT id_factura FROM factura "
                 "WHERE placas = %s")

        self.connection.query(query, (placas,))

        update_statement = ("UPDATE vehiculo "
                            "SET id_factura = COALESCE(id_factura, %s) "
                            "WHERE placas = %s")

        for id_factura in self.connection.cursor:
            self.connection.update(update_statement, (id_factura[0], placas))

    def gen_poliza(self, **data):
        costo_vehiculo = self.get_costo_vehiculo(data['id_factura'])

        prima = costo_vehiculo * 0.85
        data['prima_asegurada'] = data.get('prima_asegurada', prima)

        costo_seguro = costo_vehiculo * (6.67/12)/100
        data['costo_seguro'] = data.get('costo_seguro', costo_seguro)

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

    def search_poliza(self, **data):
        clauses = self.where_helper(data)

        query = ("SELECT * " 
                 "FROM poliza "
                 "WHERE " + clauses)

        self.connection.query(query, dictionary=True)
        return self.connection.fetchone()

    def get_costo_vehiculo(self, id_factura):
        query = ("SELECT costo_vehiculo FROM factura "
                 "WHERE id_factura = %s")

        self.connection.query(query, (id_factura,))

        return self.connection.cursor.fetchone()[0]

    def query_all(self, all_fields):
        # all_fields = {
        #     # Clientes
        #     "id_cliente": True,
        #     "nombre": True,
        #     "direccion": True,
        #     # Pólizas
        #     "costo_seguro": True,
        #     "prima_asegurada": True,
        #     "fecha_apertura": True,
        #     "fecha_vencimiento": True,
        #     # Facturas
        #     "id_factura": True,
        #     "costo_vehiculo": True,
        #     # Vehículos
        #     "placas": True,
        #     "marca": True,
        #     "modelo": True
        # }

        fields, values = self.str_helper(all_fields)

        query = ("SELECT " + fields + " "
                 "FROM cliente "
                 "NATURAL JOIN poliza "
                 "NATURAL JOIN factura "
                 "NATURAL JOIN vehiculo"
                 )

        self.connection.query(query)
