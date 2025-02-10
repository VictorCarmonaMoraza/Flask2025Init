from flask import Flask, request

app = Flask(__name__)

## la decoracion @ se denomina decorador
## la barra solo se considera la pagina de inicio
## http://localhost:5000/
@app.route('/')
def inicio():
    app.logger.debug('Mensaje a nivel debug')
    app.logger.info(f'Entramos al path {request.path}')
    app.logger.warn('Mensaje a nivel warning')
    app.logger.error('Mensaje a nivel error')
    return 'Hola Mundo desde Flask desde sevilla'