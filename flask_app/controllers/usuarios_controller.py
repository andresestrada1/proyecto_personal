from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, redirect,session, request, jsonify
from flask_app import app

from flask_app.models.usuarios import Usuario

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/inicia_sesion')
def inicia_sesion():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('registro.html')


@app.route('/registro', methods=['POST'])
def registro():
    

    if len(request.form['nombre_completo']) < 5:
        return  jsonify(message='Escribe tu nombre completo')
            
    if len(request.form['alias']) <1:
        return jsonify(message='Escribe tu alias')

    if not EMAIL_REGEX.match(request.form['email']):
        return jsonify(message='Email invalido')


    query = "SELECT * FROM usuarios WHERE email = %(email)s"
    results = connectToMySQL('proyecto_personal').query_db(query, request.form)
    if len(results) >= 1:
        return jsonify(message='El email ya existe')

    if len(request.form['contraseña']) < 6:
        return jsonify(message='La contraseña debe contener al menos 6 caracteres')

    if request.form['contraseña'] != request.form['confirma_contraseña']:
        return jsonify(message='Las contraseñas no coinciden')


    

    secret = bcrypt.generate_password_hash(request.form['contraseña'])

    formulario = {
        "nombre_completo": request.form['nombre_completo'],
        "alias": request.form['alias'],
        "email": request.form['email'],
        "contraseña":secret
    }

    Usuario.save(formulario)

    return jsonify(message='validado')
    



@app.route('/login', methods=['POST'])
def login():


    if len(request.form["email"]) < 1:
        return jsonify(message="Email requerido")


    user = Usuario.get_by_email(request.form)
    if not user:
        return jsonify(message='Email no registrado')

    if len(request.form['password']) < 1:
        return jsonify(message="Escribe tu contraseña")

    if not bcrypt.check_password_hash(user[0]["contraseña"],request.form["password"]):
        return jsonify(message="Contraseña incorrecta")

    session['usuario_id'] = user[0]['id']
            
    return jsonify(message='validado')
    # return render_template('bienvenido.html',user=user)

@app.route('/cerrar_sesion')
def cerrar():
    session.clear
    return redirect('/')
