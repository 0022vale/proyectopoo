from genericoCompra import GenericoCompra
from metodosCompra import MetodosCompra
def menuCompra():
    avanzar = True
    while (avanzar):
        correcta = False
        while(not correcta):
            print('............Menu Principal Compra...........')
            print(' "1" Listar Compra: ')
            print(' "2" Registrar Compra: ')
            print(' "3" Acualizar Compra: ')
            print(' "4" Eliminar Compra: ')

            opcion = int(input('Ingrese una de las opciones: '))
            if opcion < 1 or opcion > 4:
                print('Opcion invalida.  Ingrese una opcion correcta menu compra: ')
            elif opcion == 5:
                avanzar = False
                print ('Gracias. Que tenga buen dia')
                break
            else:
                correcta = True
                opciones(opcion)



def opciones(opcion):
    genericoCompra = GenericoCompra()
    metodosCompra =  MetodosCompra()
    if opcion == 1:
        try:
            compra = genericoCompra.listarCompras()
            if len(compra) > 0:
                metodosCompra.listarCompras(compra)
            else:
                print('No se encontraron registros')

        except:
            print('Ocurrio un error en listar')

    if opcion == 2:
        compra = metodosCompra.registroCompras()
        try:
            genericoCompra.registroCompra(compra)
        except:
            print('Ocurrio un error al registrar')  
              
    elif  opcion == 3:
        try:
            compra = genericoCompra.listarCompras()
            if len(compra) > 0:
                compra = metodosCompra.compraActualizar(compra)
                if compra:
                    genericoCompra.actualizarCompra(compra)
                else:
                    print('No se encontro el id de la Compra que desea modificar')    
            else:
                print('no se encontraron compras')
        except:
            print('ocurrio un error con la modificacion Compra')   
  
    #if opcion == 3:
     #     pass
        #print('Acualizar Compra: ')

    elif opcion == 4:
        try:
            compra = genericoCompra.listarCompras()
            if len(compra) > 0:
                codigoidCompEliminar = metodosCompra.eliminarCompras(compra)
                if not(codigoidCompEliminar == ""):
                    genericoCompra.eliminarCompra(codigoidCompEliminar)
                else:
                    print('No se encontro ID de la Compra')
            else:
                print('No se encontro la Compra') 
        except:
            print('Ocurrio un error con la Compra eliminado')                   

        #print('Eliminar Compra: ')

menuCompra()
#if opcion == 1:
#    print('Listar Compra')
#elif opcion == 2:
#    print('Registro Compra')
#elif opcion == 3:
#    print('Actualizacion Compra')
#elif opcion == 4:
#    print('Eliminacion Compra')
