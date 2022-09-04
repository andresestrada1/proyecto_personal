from flask import render_template, redirect,session, request, jsonify
from flask_app import app
from flask_app.models.poemas import Poema
from flask_app.models.usuarios import Usuario



@app.route('/nuevo_poema')
def guardar():
    return render_template('nuevo_poema.html')


@app.route('/crear_poema', methods=['POST'])
def crear_poema():
    print('mas cerveza')
    
    if len(request.form['titulo_poema']) < 1:
        return jsonify(message='Agrega un titulo a tu poema')

    if len(request.form['poema']) < 30:
        return jsonify(message='Escribe tu poema')

    formulario = {
        "titulo_poema": request.form['titulo_poema'],
        "poema": request.form['poema'],
        "usuario_id":session['usuario_id']
    }


    Poema.guardar_poema(formulario)
    return jsonify(message='validado')

    # return render_template('bienvenido.html')

@app.route('/bienvenido')
def bienvenido():

    if not session:
        return redirect('/')
    
    datos = []

    
    poemas = Poema.obtener_poemas()
    for poema in poemas:
        formulario = {
            'id':poema['usuario_id']
        }
        dato = {
            'titulo_poema':poema['titulo_poema'], 
            'autor': Usuario.get_name_by_id(formulario),
            'id_poema': poema['id'],
            'id_creador_poema': poema['usuario_id']
        }

        datos.append(dato)
    
    autor = Usuario.get_name_by_id({'id':session['usuario_id']})
    

    return render_template('bienvenido.html',datos=datos, autor= autor )

@app.route('/mostrar_poema/<int:id_poema>/<int:id_creador_poema>')
def mostrar_poema(id_poema, id_creador_poema):
    if not session:
        return redirect('/')
    
    formulario = {'id': id_poema}
    
    
    poema = Poema.obtener_poema(formulario)
    
    creador = Usuario.get_name_by_id({'id':id_creador_poema})
    
    
    datos = {
        'poema': poema['poema'],
        'titulo_poema': poema['titulo_poema'],
        'creador':creador,
        'id_creador':id_creador_poema, 
        'id_sesion': session['usuario_id'],
        'id_poema': id_poema
    }

    return render_template('poemas.html', datos=datos)

    
@app.route('/actualizar/poema/<int:id_poema>')
def actualizar_poema(id_poema):
    if not session:
        return redirect('/')

    formulario = {'id': id_poema}
    
    poema = Poema.obtener_poema(formulario)
    
    datos = {
        'poema': poema['poema'],
        'titulo_poema': poema['titulo_poema'],
        'poema_id': id_poema,
        'creador_id': poema['usuario_id']
    }

    return render_template('actualizar.html', datos = datos )

@app.route('/modificar_poema', methods= ['POST'])
def modificar_poema():
    

    formulario = {
        'titulo_poema': request.form['titulo_poema'],
        'poema': request.form['poema'],
        'id': request.form['poema_id']
    }

    id_poema = request.form['poema_id']
    id_creador = request.form['creador_id']

    Poema.actualizar_poema(formulario)
    
    return redirect(f'/mostrar_poema/{id_poema}/{id_creador}')

    

@app.route('/eliminar/<int:id_poema>')
def eliminar(id_poema):
    formulario = {
            'id': id_poema
        }
    
    Poema.eliminar(formulario)
    return redirect('/bienvenido')