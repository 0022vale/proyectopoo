#App archivo principal/arrancar la aplicacion de nuestro servidor.
#importamos flask para obtener un objeto/una conexion (configurar)

from flask import Flask, redirect,render_template,request, url_for,flash 
from flask_mysqldb import MySQL # permite modulo conexion a base de datos 
#pasamos el parametro name
app = Flask(__name__)

#conexion:para ejecutarlo pasamos las configuracione/parametros donde esta la bd nombre, usuario etc.
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tp_poo_vale'
mysql = MySQL(app) #variable7 (app inicializacion a db)

#proteger la sesion/guardarlo en el servidor para reutilizarlo 
app.secret_key = 'mysecretkey'

#ruta principal de nuestra aplicacion:creamos funcion index, retorna:
@app.route('/')
def Index(): #el html enviara al index ruta para hacer la consulta
    cur = mysql.connection.cursor() #consulta a la base de datos
    cur.execute('SELECT * FROM cliente')#consulta obtener todos los datos
    datos = cur.fetchall() #obtener todos los datos con fetchall y guardo en variable datos
    return render_template('index.html', cliente = datos)#paso los datos al indice de html obtenidos de la bd
    #retorne/renderice la plantilla(nombre del archivo index.html/form)


#ruta agregar contactos/permite agregar. funcion. los datos ingresados de form #
# metodo post:datos no visibles 
@app.route('/agregarCliente', methods =['POST'])
def agregarCliente():
    if request.method == 'POST':#si a traves del metodo post (ruta agregarcliente) 
        ID = request.form['id'] #y recibo  y guardo datos(valor) del form con variable
        NOMBRE = request.form['nombre']
        APELLIDO = request.form['apellido']
        DNI = request.form['dni']
        EMAIL = request.form['email']
        DIRECCION = request.form['direccion'] #mysql quiero tu conexion solo el cursor
        cur = mysql.connection.cursor()# almacena los datos en bd en la variable cur y las ejecuto y le paso los valores de los campos tupla
        cur.execute('INSERT INTO cliente (id,nombre,apellido,dni,email,direccion) VALUES (%s, %s, %s, %s, %s, %s)', (ID, NOMBRE, APELLIDO, DNI, EMAIL, DIRECCION))
        mysql.connection.commit() #arriba escribo la consulta y con el commit la ejecuto
        flash('El cliente se agrego correctamente')#flash permite mandar mensaje entre vistas(flask)
        return redirect(url_for('Index'))#redireccionamos y le damos la ruta principal Index(url)recetea y vuelve

#ruta obtener/. Creamos otro formulario para mostrarlo y modificarlos los datos   
@app.route('/editarCliente/<id>') #pasamos parametro id
def obtenerCliente(id): # recibimos ese id
    cur = mysql.connection.cursor() #consulta a la base de datos
    cur.execute("SELECT * FROM cliente  WHERE id = %s" % (id)) #selecioname de la tabla... el id que sea igual al id que te pase x parametro
    datos = cur.fetchall() # obtendre datos de un unico valor (que quiere modificar)                                  
    print(datos)#quiero la lista del indice 0
    return render_template('cliente_editar.html', cliente = datos[0]) #paso los datos al indice de html obtenidos de la bd
    #retorne/renderice la plantilla(nombre del archivo cliente_editar.html/form)
    
#una vez obtenidos los datos creamos ruta de actualizarCliente y
    #tb en cliente_editar.html le pasamos la ruta el indice. 0 y el metodo post  
@app.route('/actualizarCliente/<id>', methods = ['POST'])
def actualizarCliente(id):
    if request.method == 'POST': # si recibo datos a traves del metodo post(/cliente editar)
        NOMBRE = request.form['nombre'] #y recibo  y guardo datos(valor) del form con variable
        APELLIDO = request.form['apellido']
        DNI = request.form['dni']
        EMAIL = request.form['email']
        DIRECCION = request.form['direccion']
        cur = mysql.connection.cursor() #consulta a la base de datos y luego la consulta de actualizacion con los datos que le pasamos
        cur.execute("""  
          UPDATE cliente
          SET nombre = %s,
              apellido = %s,
              dni = %s,
              email = %s,
              direccion = %s
          WHERE id = %s
        """,(NOMBRE,APELLIDO,DNI,EMAIL,DIRECCION,id))
        mysql.connection.commit() # ejercuto la consulta
        flash('El cliente se actualizo') 
        return redirect(url_for('Index')) #redireccionamos y le damos la ruta principal Index(url)recetea y vuelve   

#ruta eliminar: /pasamos parametro que es un string de tipo id
@app.route("/eliminarCliente/<string:id>") # cada vez que reciba un parametro debe tener un num para eliminarlo
def eliminarCliente(id): #pasamos parametro(id)
    cur = mysql.connection.cursor() #consulta a la base de datos
    cur.execute('DELETE FROM cliente WHERE id = {0}'.format(id)) #consulta eliminame en esta posicion 0 ira el id formateado a un string para pasarle a la ocnsulta bd mysql
    mysql.connection.commit() #ejercuto consulta 
    flash('El cliente se elimino correctamente')
    return redirect(url_for('Index')) #redireccionamos y le damos la ruta principal Index(url)recetea y vuelve

#archivo principal: validacion:(name:constante de python es igual a main.
#Es decir si el archivo que se esta ejecutando es App.py empieza a ejecutar nuestro servidor)        
if __name__ =='__main__':
    app.run(port= 3000, debug=True)
     #para empezar a ejecutar nuestro servidor app.run= el puerto sera 3000,
     #usamos debug de flask nos permite reiniciar:los cambios que realizamos
     #a traves del servidor esto reinicia automaticamente.
