from flask import Flask

servidor = Flask(__name__)

@servidor.route('/')
def hola():
    return "Hola desde servidor 3"

if __name__ == '__main__':
    servidor.run(host='0.0.0.0', port=5004) # Change port to 5003