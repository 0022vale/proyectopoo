


class MetodosCliente(): #creamos metodos para recargar todas las funcionalidades en menu
    def listarClientes(self,cliente):
        contador= 1
        for cli in cliente:#creamos un for recorre la lista
            datos = "{0}.NOMBRE: {1} APELLIDO: {2} DNI: {3} EMAIL: {4} DIRECCION: {5}"
            print(datos.format( cli[0],cli[1],cli[2],cli[3],cli[4],cli[5]))# pasamos indices posiciones
            contador += 1

    def registroClientes(self):
        idCorrecto = False # funcion pedir datos y registrarlos
        while (not idCorrecto):
            ID = input('Ingrese el ID del Cliente: ')# validamos que sea numerico
            if ID.isnumeric():
                if int(ID) > 0:
                    idCorrecto = True
                    ID = int(ID)
                else:
                    print('El id del Cliente debe ser un numero mayor a cero 0')
            else:
                print('Id incorrecto: El id del Cliente debe ser numerico')              
        NOMBRE = input('Ingrese nombre del cliente: ') 
        APELLIDO = input('Ingrese apellido cliente: ')
        DniCorrecto = False
        while (not DniCorrecto):# validamos que el dni tenga 8 caracteres
            DNI = (input('Ingrese el Dni del Cliente: ')) 
            if len(DNI) == 8:
                DniCorrecto = True
            else: 
                print('Dni incorrecto: El dni debe tener 8 digitos')
        EMAIL = input('Ingrese email del cliente: ')
        DIRECCION = input('Ingrese direccion del cliente: ')        
        cliente = (ID,NOMBRE,APELLIDO,DNI,EMAIL,DIRECCION )# variable le pasamos datos y nos lo retorna
        return cliente       
    
    def clienteActualizar(self,cliente):#pasamos lista y verificamos si hay
        self.listarClientes(cliente)
        existeCliente = False
        clienteEditar= int(input('Ingrese el id Cliente que desea modificar: '))
        for cli in cliente:# recorremos la lista con un for
            if cli[0] == clienteEditar:
                existeCliente = True # si hay es true continua
                break                
        
        if existeCliente: # si existe variable ingrese datos
    
            NOMBRE=input('Ingrese el Nombre del Cliente: ')
            APELLIDO=input('Ingrese el Apellido del Cliente: ')
            DniCorrecto = False
            while (not DniCorrecto):#validamos dni longitud 8 caracteres
                DNI = input('Ingrese el Dni del Cliente: ') 
                if len(DNI) == 8:
                    DniCorrecto = True
                else:
                    print('Dni incorrecto: El dni debe tener 8 digitos')
            EMAIL= input('Ingrese email del cliente: ')
            DIRECCION= input('Ingrese la Direccion del Cliente: ')                
            cliente=(clienteEditar,NOMBRE,APELLIDO,DNI,EMAIL,DIRECCION)
        else:
            cliente = None    
        return cliente         



    def eliminarClientes(self,cliente):#lista los clientescreamos variable codeeliminar
        self.listarClientes(cliente)
        existeCliente = False
        codigoidCliEliminar = int(input('Ingrese el id del Cliente que desea eliminar:'))
        for cli in cliente:# recorre el for 
            if cli[0] == codigoidCliEliminar:
                existeCliente = True
                break
        if not existeCliente:# sino existe devuelve vacio
            codigoidCliEliminar = ""    

        return codigoidCliEliminar    



        