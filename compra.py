import mysql.connector
#from cliente import Cliente
#from producto import Producto
class Compra():
    def __init__(self,id_cliente,id_producto):
        self.id=0
        self.id_cliente=id_cliente
        self.id_producto=id_producto

    @property
    def id_cliente(self):
        return self.id_cliente

    @property
    def id_producto(self):
        return self.id_producto

    @id_cliente.setter
    def id_cliente(self):
        self.id_cliente = self.id_cliente

    @id_producto.setter
    def id_producto(self):
        self.id_producto = self.id_producto    
