class MetodosCompra():
    def listarCompras(self,compra):
        contador = 1
        for comp in compra:
            datos = "id: {} id_cliente: {} id_producto: {}"
            print(datos.format(comp[0],comp[1],comp[2]))
            contador += 1

    def registroCompras(self):
        idCorrecto = False
        while (not idCorrecto):
            ID = input('Ingrese el ID de la Compra: ')
            if ID.isnumeric():
                if int(ID) > 0:
                    idCorrecto = True
                    ID = int(ID)
                else:
                    print('El ID de la Compra debe ser un numero mayor a cero 0')
            else:
                print('ID incorrecto: El id de la Compra debe ser numerico')
        IDCLIENTE =int(input('Ingrese el id del Cliente: '))
        IDPRODUCTO =int(input('Ingrese el id del Producto: '))
        compra = (ID,IDCLIENTE,IDPRODUCTO)
        return compra       

    def compraActualizar(self,compra):
        self.listarCompras(compra)
        existeCompra = False
        compraEditar= int(input('Ingrese id la Compra que desea modificar: '))
        for comp in compra:
            if comp[0] == compraEditar:
                existeCompra = True
                break
        if existeCompra:
            IDCLIENTE =int(input('Ingrese el id del Cliente que desea modificar: '))
            IDPRODUCTO =int(input('Ingrese el id del Producto que desea modificar: '))
            compra = (compraEditar,IDCLIENTE,IDPRODUCTO)                        
        else:
            compra = None    
        return compra        


    def eliminarCompras(self,compra):
        self.listarCompras(compra)
        existeCompra = False
        codigoidCompEliminar = int(input('Ingrese el id de la Compra que desea eliminar:'))
        for comp in compra:
            if comp[0] == codigoidCompEliminar:
                existeCompra = True
                break
        if not existeCompra:
            codigoidCompEliminar = ""    
        return codigoidCompEliminar       