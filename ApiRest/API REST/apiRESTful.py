from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# URL base de la API externa (mock API)
API_URL = "https://66eb023b55ad32cda47b5184.mockapi.io/IoTCarStatus"

# Obtener todos los registros (Read - GET)
@app.route('/cars', methods=['GET'])
def get_all_cars():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Error fetching data'}), response.status_code

# Obtener un solo registro por ID (Read - GET)
@app.route('/cars/<int:id>', methods=['GET'])
def get_car(id):
    response = requests.get(f"{API_URL}/{id}")
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Car not found'}), response.status_code

# Crear un nuevo registro (Create - POST)
@app.route('/cars', methods=['POST'])
def create_car():
    data = request.get_json()
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify({'error': 'Failed to create car'}), response.status_code

# Actualizar un registro existente por ID (Update - PUT)
@app.route('/cars/<int:id>', methods=['PUT'])
def update_car(id):
    data = request.get_json()
    response = requests.put(f"{API_URL}/{id}", json=data)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to update car'}), response.status_code

# Eliminar un registro por ID (Delete - DELETE)
@app.route('/cars/<int:id>', methods=['DELETE'])
def delete_car(id):
    response = requests.delete(f"{API_URL}/{id}")
    if response.status_code == 200:
        return jsonify({'message': 'Car deleted successfully'})
    else:
        return jsonify({'error': 'Failed to delete car'}), response.status_code

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
