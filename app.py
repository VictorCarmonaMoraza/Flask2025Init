from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)

app.secret_key='Mi_llave_secreta'

## la decoracion @ se denomina decorador
## la barra solo se considera la pagina de inicio
## http://localhost:5000/
@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario ya ha hecho login {session["username"]}'
    return 'No ha hecho login.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
    ## recuperamos usuario y password de sesion
        usuario = request.form['username']
        #agregar usuario a la session
        session['username'] =usuario
        ##session['username'] =request.form['username']
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.route('/saludar')
def saludar():
    return 'Saludos'

@app.route('/saludarnombre/<nombre>')
def saludarnombre(nombre):
    return f'Saludos {nombre}'


@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'La edad es {edad}'

@app.route('/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_nombre(nombre):
    return f'Tu nombre es: {nombre}'

@app.route('/mostrarvalores/<nombre>', methods=['GET','POST'])
def mostrar_valores(nombre):
    return render_template('mostrar.html')

@app.route('/mostrarvaloresplantilla/<nombre>', methods=['GET','POST'])
def mostrar_valores_plantiila(nombre):
    return render_template('mostrar.html', parametro = nombre)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('inicio'))

@app.route('/redireccionar2')
def redireccionar2():
    return redirect(url_for('mostrar_nombre', nombre='juan'))

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return (render_template('error404.html', error_variable= error), 404)

#REST Representational state transfer
# api/mostrar/victor
@app.route('/api/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_json(nombre):
    ## Crear diccionario
    valores = {'nombre': nombre, 'metodo_http':request.method}
    ## Devuelve un diccionario
    return jsonify(valores)




