import mysql.connector
from mysql.connector import errorcode


class MySQLConnector:
    connection = None
    config = {
        'user': 'root',
        'password': 'password',
        'host': 'localhost',
        'database': 'proyecto',
        'raise_on_warnings': True
    }

    def __init__(cls, *args, **kargs):
        if cls.connection is None:
            try:
                cls.cnx = mysql.connector.connect(**self.config)

            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)
        return cls.instance