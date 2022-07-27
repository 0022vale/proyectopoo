

from flask import Flask, redirect,render_template,request, url_for,flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tp_poo_vale'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM producto')
    datos = cur.fetchall()
    print(datos)
    return render_template('index.html', producto = datos)

@app.route('/agregarProducto',methods = ['POST'])
def agregarProducto():
    if request.method == 'POST':
        ID = request.form['id']   
        NOMBRE = request.form['nombre']
        DESCRIPCION = request.form['descripcion']
        PRECIO = request.form['precio']
        print(ID)
        print(NOMBRE)
        print(DESCRIPCION)
        print(PRECIO)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO producto (id,nombre,descripcion,precio) VALUES (%s, %s, %s, %s)', (ID, NOMBRE, DESCRIPCION, PRECIO) )
        mysql.connection.commit()
        flash('El producto se agrego correctamente')
        return redirect(url_for('Index'))
    
@app.route('/editarProducto/<id>')
def obtenerProducto(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM producto WHERE id = %s" % (id))
    datos = cur.fetchall()
    print(datos)
    return render_template('producto_editar.html', producto = datos[0] )
    #return 'recibido'
@app.route('/actualizarProducto/<id>', methods = ['POST'])
def actualizarProducto(id):
    if request.method == 'POST':
        NOMBRE = request.form['nombre']
        DESCRIPCION = request.form['descripcion']
        PRECIO = request.form['precio']
        cur = mysql.connection.cursor()
        cur.execute("""
                    UPDATE producto
                    SET nombre = %s,
                        descripcion = %s,
                        precio = %s
                    WHERE id = %s
                        """,(NOMBRE,DESCRIPCION,PRECIO,id))
        mysql.connection.commit()
        flash('El producto se actualizo correctamente')
        return redirect(url_for('Index'))



@app.route('/eliminarProducto/<string:id>')
def eliminarProducto(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM producto WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('El producto se elimino correctamente')
    return redirect(url_for('Index'))

        
if __name__ =='__main__':
    app.run(port= 3000, debug=True)
