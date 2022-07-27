from genericoProducto import GenericoProducto
from metodosProducto import MetodosProducto

def menuProducto():
    avanzar = True
    while (avanzar):
        correcta = False
        while(not correcta):
            print('............Menu Principal Producto...........')
            print(' "1" Listar Producto: ')
            print(' "2" Registrar Producto: ')
            print(' "3" Actualizar Producto: ')
            print(' "4" Eliminar Producto: ')

            opcion = int(input('Ingrese una de las opciones: '))
            if opcion < 1 or opcion > 4:
                print('Opcion invalida.  Ingrese una opcion correcta: ')
            elif opcion == 5:
                avanzar = False
                print ('Gracias. Que tenga buen dia')
                break
            else:
                correcta = True
                opciones(opcion)



def opciones(opcion):
    genericoProducto = GenericoProducto()
    metodosProducto =  MetodosProducto()
    if opcion == 1:
        try:
            producto = genericoProducto.listarProductos()
            if len(producto) > 0:
                metodosProducto.listarProductos(producto)
            else:
                print('No se encontraron registros')

        except:
            print('Ocurrio un error en listar')

    if opcion == 2:
        producto = metodosProducto.registroProductos()
        try:
            genericoProducto.registroProducto(producto)
        except:
            print('Ocurrio un error al registrar')    

    elif  opcion == 3:
        try:
            producto = genericoProducto.listarProductos()
            if len(producto) > 0:
                producto = metodosProducto.productoActualizar(producto)
                if producto:
                    genericoProducto.actualizarProducto(producto)
                else:
                    print('No se encontro el id del Producto que desea modificar')    
            else:
                print('')
        except:
            print('ocurrio un error con la modificacion Producto')   
  
    #if opcion == 3:
       #pass
       #print('Acualizar Producto: ')
    elif opcion == 4:
        try:
            producto = genericoProducto.listarProductos()
            if len(producto) >0:
                codigoidProEliminar = metodosProducto.eliminarProductos(producto)
                if not(codigoidProEliminar == ""):
                    genericoProducto.eliminarProducto(codigoidProEliminar)
                else:
                    print('No se encontro ID del Producto')
            else:
                print('No se encontro Producto') 
        except:
            print('Ocurrio un error con el Producto eliminado')                   

        
    
    
    


menuProducto()

#if opcion == 1:
#    print('Listar Producto')
#elif opcion == 2:
#    print('Registro Producto')
#elif opcion == 3:
#    print('Actualizacion Producto')
#elif opcion == 4:
#    print('Eliminacion Producto')


