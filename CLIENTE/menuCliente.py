from genericoCliente import GenericoCliente #importo metodosCliente para utilizar funciones
from metodosCliente import MetodosCliente

def menuCliente(): #creamos un metodoy lo llamamos menu sera el principal y encargado de mostrarnos el menu
    avanzar = True#creamos variable avanzar si es verdadero el usuario puede continuar
    while (avanzar):# preguntamos mientras sera true
        correcta = False # creamos variable correcta al momento de iniciar el menu no tenemos opcion seleccionada
        while(not correcta):#mientras no sea la opcion correcta volvemos a mostrar el menu
            print('............Menu Principal Cliente...........')#imprimimos funciones principales
            print(' "1" Listar Cliente: ')
            print(' "2" Registrar Cliente: ')
            print(' "3" Actualizar Cliente: ')
            print(' "4" Eliminar Cliente: ')

            opcion = int(input('Ingrese una de las opciones: '))#a traves de la variable opcion seleccione cual quiere
            if opcion < 1 or opcion > 4:#si es mayor o menor a 4 imprimimos incorrecta
                print('Opcion invalida.  Ingrese una opcion correcta: ')
            elif opcion == 5:#si ingresa 5 no desea continuar
                avanzar = False
                print ('Gracias. Que tenga buen dia')
                break
            else:# si ejecuta 1,2,3,4 verdadera avanza
                correcta = True
                opciones(opcion)



def opciones(opcion):#retorna a traves de metodos () los indices que le pasamos
    genericoCliente= GenericoCliente()#llamamos a traves de variable cliente el metodolistar que es propio de generico que es un objeto de la clase generico(instancia)
    metodosCliente= MetodosCliente()
    if opcion == 1:
        try:
            cliente = genericoCliente.listarClientes()
            if len(cliente) > 0:#preguntamos la longitud 
                metodosCliente.listarClientes(cliente)
            else:
                print('No se encontraron registros')

        except:
            print('Ocurrio un error en listar')

    if opcion == 2:# pasamos datos ingresados a traves de metodosCli con el metodo registrar(archivo)
        cliente = metodosCliente.registroClientes()
        try:
            genericoCliente.registroCliente(cliente)#generico es la conexion de bd co el metodoscli
        except:
            print('Ocurrio un error al registrar')    

    
    elif  opcion == 3:#cuando verificamos que tenemos algo en la lista lee su longitud y llamamos a generico la conexion
        try:
            cliente = genericoCliente.listarClientes()
            if len(cliente) > 0:
                cliente = metodosCliente.clienteActualizar(cliente)
                if cliente:
                    genericoCliente.actualizarCliente(cliente)
                else:
                    print('No se encontro el id del Cliente que desea modificar')    
            else:
                print('no se encontraron clientes')
        except:
            print('ocurrio un error con la modificacion Cliente')   

        #pass
       # print('Acualizar Cliente: ')
       
    elif opcion == 4:# a traves del try llamamos a la lista, llamamos a generico conexion. creamos variable codigo eliminar comprobamos si esta vacio. si es un codigo valido elimina
        try:
            cliente = genericoCliente.listarClientes()
            if len(cliente) > 0:
                codigoidCliEliminar = metodosCliente.eliminarClientes(cliente)
                if not(codigoidCliEliminar == ""):
                    genericoCliente.eliminarCliente(codigoidCliEliminar)
                else:
                    print('No se encontro ID del Cliente')
            else:
                print('No se encontro Cliente') 
        except:
            print('Ocurrio un error con el Cliente eliminado')                   

        #print('Eliminar Cliente: ')

menuCliente()




