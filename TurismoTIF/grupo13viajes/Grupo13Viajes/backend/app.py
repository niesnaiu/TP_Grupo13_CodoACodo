from flask import Flask
from flask import render_template, redirect, request, Response, session #logging, flash
from flask_mysqldb import MySQL
#from urllib.parse import quote as url_quote

from flask.globals import app_ctx

app = Flask(__name__, template_folder='template')

#configuración MySQL
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='clientes'
app.config['MYSQL_CURSORCLASS']='DictCursor'

#INIT MYSQL
mysql=MySQL(app)

#
@app.route('/')
def home():
    return render_template('./login.html') #retorna al html del login

#@app.route('/admin.html')
#def admin():
    #return render_template('./admin.html') 


#@app.route('/login.html, methods= ["GET","POST"]')
#def register():
    #form = RegisterForm(request.form)
        #name = form.name.data
        #email = form.email.data
        #password = sha256_crypt.encrypt(str(form.password.data))

        #cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO registros(name, email, password) VALUES(%, %, %)",  (name, email, password))

        #commit a la BD
        #mysql.connection.commit()

        #cierre de la conexión
        #cur.close()

        #flash("Usuario registrado exitosamente")

        


#def login():

    #if request.methods == 'POST' and 'txtCorreo' in request.form and 'txtPassword':
        #_correo = request.form['txtCorreo']
        #_password = request.form['txtPassword']

    #cur=mysql.connection.cursor()  #conecta a la bd
    #cur.execute('SELECT * FROM registros WHERE correo = %s AND password = %s,(_correo, _password,)')
    #account = cur.fetchone()

    #if account:
        #session['logueado'] = True
        #session['id'] = account['id']

        #return render_template("./login.html")
    #else:       

        #return render_template('./admin.html') #retorna al html del login


if __name__ == '__main__':
    app.secret_key="grupo_trece"
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)