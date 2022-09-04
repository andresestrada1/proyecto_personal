
from flask_app.config.mysqlconnection import connectToMySQL

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import jsonify

class Usuario:

    def __init__(self,data):
        self.id = data['id']
        self.nombre_completo = data['nombre_completo']
        self.alias = data['alias']
        self.email = data['email']
        self.contraseña = data['contraseña']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,formulario):
        query = "INSERT INTO usuarios(nombre_completo, alias, email, contraseña) VALUES (%(nombre_completo)s,%(alias)s,%(email)s,%(contraseña)s)"
        result = connectToMySQL('proyecto_personal').query_db(query, formulario)
        print(result)
        return result

    @classmethod
    def get_by_email(cls, formulario):
        query = "SELECT * FROM usuarios WHERE email = %(email)s"
        result = connectToMySQL('proyecto_personal').query_db(query, formulario)
        return result

    @classmethod
    def get_name_by_id(cls, formulario):
        query = "SELECT nombre_completo FROM usuarios WHERE id = %(id)s" 
        result = connectToMySQL('proyecto_personal').query_db(query, formulario)
        return result[0]['nombre_completo']