from mysql.connector import Error
from mysql.connector import Error
import mysql.connector

class GenericoProducto:
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

    def listarProductos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM producto")
                respuesta=cursor.fetchall()
                return respuesta
            except Error as ex:
                print('No se pudo listar producto: {0}'.format(ex))

    def registroProducto(self,producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("INSERT INTO producto(id,nombre,descripcion,precio) VALUES ( {0},'{1}','{2}',{3})") 
                cursor.execute(sql.format(producto[0],producto[1],producto[2],producto[3]))
                self.conexion.commit()
                print('El Producto se registro correctamente')

            except Error as ex:
                print('Error en el intento: {0}'.format(ex))

    def actualizarProducto(self,producto):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql= "UPDATE producto SET nombre = '{0}', descripcion = '{1}', precio = {2} WHERE id = {3}"
                cursor.execute(sql.format(producto[1],producto[2],producto[3],producto[0]))            
                self.conexion.commit()  
                print('el Producto se actualizo correctamente')
            except Error as ex:
                 print('Error en el intento de actualizar Producto: {0}'.format(ex))   
        

    def eliminarProducto(self,idProductoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM producto WHERE id = {0}"
                cursor.execute(sql.format(idProductoEliminar))
                self.conexion.commit()
                print('El Producto se ha eliminado')            
            except Error as ex:
                print('Error en el intento: {0}'.format(ex))
                