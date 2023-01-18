from flask import Blueprint, jsonify, request
from models.entities.Usuario import Usuario
from models.UsuarioModel import UsuarioModel

import uuid

main = Blueprint('usuarios_blueprint', __name__)

status = ['nameSystem: api-users', 'version: 0.0.1', 'developer: Juan Carlos Condori Machicado', 'email: juan.com@gmail.com']

@main.route('/')
def get_usuarios():
    try:
        usuarios = UsuarioModel.get_usuarios()
        return jsonify(usuarios)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/promedio-edad/')
def get_promedio():
    try:
        edad = UsuarioModel.get_promedio()
        return jsonify(edad)
    except Exception as ex:
        edad = UsuarioModel.get_promedio()
        print(edad)
        return jsonify({'message':str(ex)}),500

@main.route('/status/')
def get_status():
    try:
        return jsonify(status)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/add', methods=['POST'])
def add_usuario():
    try:
        name = str(request.json['name'])
        age = request.json['age']
        id = uuid.uuid4()
        print(id)
        usuario = Usuario(str(id),name,age)

        affected_rows = UsuarioModel.add_usuario(usuario)

        if affected_rows ==1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message':'ERROR INSERT'}),500
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/update/<id>', methods=['PUT'])
def update_usuario(id):
    try:
        name = request.json['name']
        age = request.json['age']
        usuario = Usuario(id, name, age)

        affected_rows = UsuarioModel.update_usuario(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message': "No usuario updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        usuario = Usuario(id)

        affected_rows = UsuarioModel.delete_usuario(usuario)

        if affected_rows ==1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message':'NO MOVIE DELETED'}),500
    except Exception as ex:
        return jsonify({'message':str(ex)}),500