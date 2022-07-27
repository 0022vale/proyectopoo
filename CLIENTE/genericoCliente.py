from mysql.connector import Error # encargado de hacer la conexion generico 
from mysql.connector import Error# en caso de q de error importo
import mysql.connector #importo la conexion a bd my sql

class GenericoCliente:# creamos clase para que pueda listar,registrar modificar y eliminar
    def __init__(self):# cuando se instancie esta clase llamara a su constructor, realizara conexion y se acumulara 
        try: # en la variableconexion
            self.conexion= mysql.connector.connect(# pasamos parametros
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                database = 'tp_poo_vale'
            )
        except Error as ex:
            print('No se pudo concretar la conexion: {0}'.format(ex))# caso error lo concateno con format ex

    def listarClientes(self):
        if self.conexion.is_connected():#pregutamos si estamos conectados
            try:
                cursor= self.conexion.cursor()
                cursor.execute("SELECT *FROM cliente ORDER BY id DESC")
                respuesta=cursor.fetchall()# cursor fechall retorna toda la lista
                return respuesta
            except Error as ex:
                print('No se pudo listar: {0}'.format(ex))

    def registroCliente(self,cliente):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql= ("INSERT INTO cliente(id,nombre,apellido,dni,email,direccion) VALUES ({0},'{1}','{2}',{3},'{4}','{5}')") 
                cursor.execute(sql.format(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4],cliente[5]))
                self.conexion.commit()
                print('El cliente se registro correctamente')

            except Error as ex:
                print('Error en el intento: {0}'.format(ex))

    def actualizarCliente(self,cliente):
        if self.conexion.is_connected():
            try:#id = {0}
                cursor=self.conexion.cursor()# pasamos datos y valores a traves de sus indices
                sql= "UPDATE cliente SET nombre = '{0}', apellido = '{1}', dni = {2}, email = '{3}', direccion = '{4}' WHERE id = {5}"
                cursor.execute(sql.format(cliente[1],cliente[2],cliente[3],cliente[4],cliente[5],cliente[0]))            
                self.conexion.commit()  #commit confirmamos accion de guardar datos
                print('El Cliente se actualizo correctamente')
            except Error as ex:
                 print('Error en el intento de actualizar Cliente: {0}'.format(ex))   
        

    def eliminarCliente(self, idClienteEliminar):# comprobamos conexion
        if self.conexion.is_connected():# eliminamos donde el parametro indice id lo formateamos a traves de cod eliminar y elimino
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM cliente WHERE id = {0} "
                cursor.execute(sql.format(idClienteEliminar))
                self.conexion.commit()
                print('El Cliente se ha eliminado')            
            except Error as ex:
                print('Error en el intento: {0}'.format(ex))

