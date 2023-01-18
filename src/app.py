from flask import Flask, jsonify, request

from config import config

from routes import Usuarios

app = Flask(__name__)

def page_not_found(error):
    return "<h1> error de algun tipo </h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    app.register_blueprint(Usuarios.main, url_prefix = '/usuarios')

    app.register_error_handler(404,page_not_found)
    app.run()
