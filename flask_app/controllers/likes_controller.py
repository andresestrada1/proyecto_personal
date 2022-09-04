from flask import render_template, redirect,session, request, jsonify
from flask_app import app
from flask_app.models.poemas import Poema
from flask_app.models.usuarios import Usuario

@app.route("/like/<int:id_poema>")
def dar_like(id_poema):
    if not session:
        return redirect('/')
    
    # Like.crear_like(formulario)

    return