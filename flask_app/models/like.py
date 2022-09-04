from flask_app.config.mysqlconnection import connectToMySQL
from flask import jsonify

class Like:

    def __init__(self,data):
        self.poema_id = data['poema_id'],
        self.usuario_id = data['usuario_id']


    
