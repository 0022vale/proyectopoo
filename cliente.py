import mysql.connector 

#from factura import Factura 

class Cliente():
    def __init__(self,nombre,apellido,dni,email,direccion):
        self.id=0
        self.nombre= nombre 
        self.apellido= apellido 
        self.__dni= dni
        self.__email= email
        self.direccion= direccion

    
    @property
    def nombre(self):
        return self.nombre 

    @property
    def apellido(self):
        return self.apellido

    @property
    def dni(self):
       return self.__dni

    @property
    def email(self):
       return self.__email
    
    @property
    def direccion(self):
        return self.direccion

    
    @ nombre.setter
    def nombre(self):
        self.nombre= self.nombre

    @ apellido.setter
    def apellido(self):
        self.apellido= self.apellido

    @ dni.setter
    def dni(self):
        self.__dni= self.__dni

    @email.setter
    def email(self):
        self.__email= self.__email
 
    @direccion.setter
    def direccion(self):
        self.direccion= self.direccion 


    def estado(self):
        print('Este es el metodo de la clase Cliente')

    def __str__(self):
        return "Nombre Cliente: {}, Apellido Cliente: {}, DNI Cliente: {}, Email Cliente: {}, Direccion Cliente: {}".format(self.nombre,self.apellido,self.dni,self.email,self.direccion)






