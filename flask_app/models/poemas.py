from flask_app.config.mysqlconnection import connectToMySQL
from flask import jsonify

class Poema:

    def __init__(self,data):
        self.id = data['id'],
        self.titulo_poema = data['titulo_poema'],
        self.poema = data['poema'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at'],
        self.usuario_id = data['usuario_id']


    @classmethod
    def guardar_poema(cls,formulario):
        query = "INSERT INTO poemas(titulo_poema, poema, usuario_id) VALUES (%(titulo_poema)s,%(poema)s,%(usuario_id)s)"
        result = connectToMySQL('proyecto_personal').query_db(query, formulario)
        return result

    @classmethod
    def obtener_poemas(cls):
        query = "SELECT titulo_poema, usuario_id, id FROM poemas "
        result = connectToMySQL('proyecto_personal').query_db(query)
        return result
    
    @classmethod
    def obtener_poema(cls, formulario):
        query = "SELECT titulo_poema, usuario_id, poema FROM poemas WHERE id = %(id)s"
        result = connectToMySQL('proyecto_personal').query_db(query, formulario)
        return result[0]
    
    @classmethod
    def actualizar_poema(cls, formulario):
        print()
        query = "UPDATE poemas SET titulo_poema = %(titulo_poema)s, poema = %(poema)s  where id = %(id)s"
        result = connectToMySQL('proyecto_personal').query_db(query, formulario)
        return result

    @classmethod
    def eliminar(cls, formulario):
        query = "DELETE FROM poemas WHERE id = %(id)s"
        result = connectToMySQL('proyecto_personal').query_db(query, formulario)
        return result

    



