from flask import Flask

app = Flask(__name__)

## la decoracion @ se denomina decorador
## la barra solo se considera la pagina de inicio
## http://localhost:5000/
@app.route('/')
def inicio():
    return 'Hola Mundo desde Flask desde sevilñla'