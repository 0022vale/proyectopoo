
import mysql.connector
from compra import Compra
#from cliente import Cliente
#from producto import Producto
#from datetime import datetime

class Factura(Compra):
    __iva= 21
    
    def __init__(self,id_compra,unidad,fecha):
        Compra(). __init__(id_compra)        
        self.id=0
        self.unidad= unidad
        self.fecha=fecha #datetime.now()

    @property
    def id(self):
        return self.id

    @property
    def unidad(self):
        return self.unidad

    @property
    def fecha(self):
        return self.fecha

    @id.setter
    def id(self):
        self.id= self.id

    @unidad.setter
    def unidad(self):
        self.unidad= self.unidad

    @fecha.setter
    def fecha(self):
       self.fecha= self.fecha

    def a_pagar(self):
        total= self.unidad * self.precio
        impuesto= total * Factura.__iva/100
        return (total + impuesto)

