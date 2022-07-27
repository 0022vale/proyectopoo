from mysql.connector import Error
from mysql.connector import Error
import mysql.connector

class GenericoCompra:
    def __init__(self):
        try:
            self.conexion= mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                database = 'tp_poo_vale'
            )
        except Error as ex:
            print('No se pudo concretar la conexion: {0}'.format(ex))

    def listarCompras(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM compra")
                respuesta=cursor.fetchall()
                return respuesta
            except Error as ex:
                print('No se pudo listar compra: {0}'.format(ex))

    def registroCompra(self,compra):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("INSERT INTO compra(id,id_cliente,id_producto) VALUES ( {0},{1},{2})") 
                cursor.execute(sql.format(compra[0],compra[1],compra[2]))
                self.conexion.commit()
                print('La compra se registro correctamente')

            except Error as ex:
                print('Error en el intento compra: {0}'.format(ex))

    def actualizarCompra(self,compra):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql= "UPDATE compra SET id_cliente = {0}, id_producto = {1} WHERE id = {2}"
                cursor.execute(sql.format(compra[1],compra[2],compra[0]))            
                self.conexion.commit()  
                print('La Compra se actualizo correctamente')
            except Error as ex:
                 print('Error en el intento de actualizar Compra: {0}'.format(ex))   
        

    def eliminarCompra(self, idCompraEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM compra WHERE id = {0} "
                cursor.execute(sql.format(idCompraEliminar))
                self.conexion.commit()
                print('La Compra se ha eliminado')            
            except Error as ex:
                print('Error en el intento: {0}'.format(ex))
                



            