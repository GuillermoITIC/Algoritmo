from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/saludo', methods=['GET'])
def saludo():
    return jsonify({'mensaje': '¡Hola! Bienvenido a la API'})

if __name__ == '__main__':
    app.run(debug=True)

