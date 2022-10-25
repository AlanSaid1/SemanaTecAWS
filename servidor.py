#from crypt import methods

from fileinput import filename
from importlib.resources import path
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from joblib import load
import numpy as np
import os

#cargar el modelo
dt = load ('modelo.joblib')

#Generar el servidor en Flask(backend)
servidorWeb = Flask(__name__)

#Anotacion
@servidorWeb.route("/test", methods=['GET'])
def formulario():
    return render_template('index.html')

#procesar daros a través del form
@servidorWeb.route('/modeloIA', methods=["POST"])
def modeloForm():
    #procesar datos de entrada
    contenido = request.form
    print (contenido)

    datosEntrada = np.array([
        10.400, 0.430, 0.500, 2.300, 0.068,13.000,19.000, 0.996,
        contenido['pH'],
        contenido['Sulfatos'],
        contenido['Alcohol']
    ])
    #Utilizar el modelo
    resultado = dt.predict(datosEntrada.reshape(1,-1))

    return jsonify({'Resultado':str(resultado[0])})

#procesar datos de un archivo
@servidorWeb.route('/modeloFile', methods = ["POST"])
def modeloFile():
    #name = "file" es donde aplica
    f = request.files['file']
    filename = secure_filename(f.filename)
    path = os.path.join(os.getcwd(), filename)
    f.save(path)
    file = open(path, 'r')
    for line in file:

        print(line)

    return jsonify({"Resultado": "datos recibidos"})

@servidorWeb.route('/modelo', methods = ["POST"])
def model():
    #procesar datos de entrada
    content = request.json
    print(content)
    return jsonify({"resultado": "datos recibidos"})

if __name__ == '__main__':
    servidorWeb.run(debug = False, host = '0.0.0.0', port = '8080')