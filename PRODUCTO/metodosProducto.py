class MetodosProducto():
    def listarProductos(self,producto):
        contador= 1
        for pro in producto:
            datos= "ID: {} NOMBRE: {} DESCRIPCION: {} PRECIO: {} "
            print(datos.format(pro[0],pro[1],pro[2],pro[3]))
            contador+= 1

    def registroProductos(self):
        idCorrecto = False
        while (not idCorrecto):
            ID = input('Ingrese el ID del Producto: ')
            if ID.isnumeric():
                if int(ID) > 0:
                    idCorrecto = True
                    ID = int(ID)
                else:
                    print('El ID del Producto debe ser un numero mayor a cero 0')
            else:
                print('ID incorrecto: El id del Producto debe ser numerico')
       
        NOMBRE = input('Ingrese nombre del Producto: ')
        DESCRIPCION = input('Ingrese descripcion del Producto: ')
        PRECIO = int(input('Ingrese precio del Producto: '))
        producto = (ID,NOMBRE,DESCRIPCION,PRECIO)
        return producto       

    def productoActualizar(self,producto):
        self.listarProductos(producto)
        existeProducto = False
        productoEditar= int(input('Ingrese el Producto que desea modificar: '))
        for pro in producto:
            if pro[0] == productoEditar:
                existeProducto = True
                break
        if existeProducto:
            
            NOMBRE = input('Ingrese nombre del Producto: ')
            DESCRIPCION = input('Ingrese descripcion del Producto: ')
            PRECIO = int(input('Ingrese precio del Producto: ') )              
            producto = (productoEditar,NOMBRE,DESCRIPCION,PRECIO)
        else:
            producto = None    
        return producto         


    def eliminarProductos(self, producto):
        self.listarProductos(producto)
        existeProducto = False
        codigoidProEliminar = int(input('Ingrese el id del Producto que desea eliminar: '))
        for pro in producto:
            if pro[0] == codigoidProEliminar:
                existeProducto = True
                break
        if not existeProducto:
            codigoidProEliminar = ""    
        return codigoidProEliminar 