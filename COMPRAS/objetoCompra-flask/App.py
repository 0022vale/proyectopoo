
from flask import Flask, redirect,render_template,request, url_for, flash
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
    cur.execute('SELECT * FROM compra')
    datos = cur.fetchall()
    print (datos)
    return render_template('index.html', compra = datos)

@app.route('/agregarCompra',methods = ['POST'])
def agregarCompra():
    if request.method == 'POST':
        ID = request.form['id']
        IDCLIENTE = request.form['id_cliente']
        IDPRODUCTO = request.form['id_producto']
        print(ID)
        print(IDCLIENTE)
        print(IDPRODUCTO)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO  compra (id,id_cliente,id_producto) VALUES (%s, %s, %s)', (ID, IDCLIENTE, IDPRODUCTO))
        mysql.connection.commit()
        flash('La compra se agrego correctamente')
        return redirect(url_for('Index'))

@app.route('/editarCompra/<id>')
def obtenerCompra(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM compra WHERE id = %s" % (id))
    datos = cur.fetchall()
    print(datos)
    return render_template('compra_editar.html', compra = datos[0] )

@app.route('/actualizarCompra/<id>', methods = ['POST'])
def actualizarCompra(id):
    if request.method == 'POST':
        IDCLIENTE = request.form['id_cliente']
        IDPRODUCTO = request.form['id_producto']
        cur = mysql.connection.cursor()
        cur.execute("""
                    UPDATE compra
                    SET id_cliente = %s,
                        id_producto = %s
                    WHERE id = %s
                        """,(IDCLIENTE,IDPRODUCTO,id))
        mysql.connection.commit()
        flash('La compra se actualizo correctamente')
        return redirect(url_for('Index'))

@app.route('/eliminarCompra/<string:id>')
def eliminarCompra(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM compra WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('La compra se elimino correctamente')
    return redirect(url_for('Index'))

        
if __name__ =='__main__':
    app.run(port= 3000, debug=True)
