from mysql.connector import Error
from mysql.connector import Error
import mysql.connector

class DB_Compra():
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                database='tp_poo_vale'

            )
        except Error as ex:
            print('No se pudo concretar la conexion: {0}'.format(ex))

