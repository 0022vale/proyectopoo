import mysql.connector

class Producto():
    def __init__(self,nombre,descripcion,precio):
        self.id=0
        self.nombre= nombre
        self.descripcion= descripcion
        self.precio= precio
    
    @property
    def id(self):
        return self.id

    @property
    def nombre(self):
        return self.nombre

    @property
    def descripcion(self):
        return self.descripcion

    @property
    def precio(self):
        return self.precio
    
    @id.setter
    def id(self):
        self.id= self.id

    @nombre.setter
    def nombre(self):
        self.nombre= self.nombre

    @descripcion.setter
    def descripcion(self):
        self.descripcion= self.descripcion

    @precio.setter
    def precio(self):
        self.precio= self.precio

    def estado(self):
        print('Este es el metodo de la clase Producto')

    def __str__(self):
        return "ID del Producto: {}, Nombre Producto: {}, Descripcion de Producto: {}, Precio Producto: {}".format(self.id,self.nombre,self.descripcion,self.precio)
                            

