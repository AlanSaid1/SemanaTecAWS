from flask import Flask, request, jsonify, render_template

#Generar el servidor en Flask(backend)
servidorWeb = Flask(__name__)

#Anotacion
@servidorWeb.route("/test", methods=['GET'])
def formulario():
    return render_template('index.html')

if __name__ == '__main__':
    servidorWeb.run(debug = False, host = '0.0.0.0', port = '8080')