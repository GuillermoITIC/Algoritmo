from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta para manejar GET
@app.route('/saludo', methods=['GET'])
def saludo_get():
    return jsonify({'mensaje': '¡Hola! Este es un saludo por GET.'})

# Ruta para manejar POST
@app.route('/saludo', methods=['POST'])
def saludo_post():
    data = request.get_json()  # Obtener datos del cuerpo de la solicitud
    nombre = data.get('nombre', 'desconocido')  # Extraer 'nombre', o 'desconocido' si no existe
    return jsonify({'mensaje': f'¡Hola, {nombre}! Has hecho un POST correctamente.'})

# Ruta para manejar PUT
@app.route('/saludo', methods=['PUT'])
def saludo_put():
    data = request.get_json()  # Obtener datos del cuerpo de la solicitud
    nombre = data.get('nombre', 'desconocido')  # Extraer 'nombre'
    return jsonify({'mensaje': f'¡Hola, {nombre}! Has actualizado el saludo con un PUT.'})

# Ruta para manejar DELETE
@app.route('/saludo', methods=['DELETE'])
def saludo_delete():
    return jsonify({'mensaje': '¡Has borrado el saludo con DELETE!'})

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
