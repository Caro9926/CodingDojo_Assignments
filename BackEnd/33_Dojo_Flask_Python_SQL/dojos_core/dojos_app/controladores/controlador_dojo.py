from flask import Flask, render_template, request, redirect, session 
from dojos_app import app

from dojos_app.modelos.modelo_dojo import Dojo  #importo la clase

@app.route( '/', methods=['GET'] )
def mostrarDojos():
    return redirect('/dojos')

@app.route( '/dojos', methods=["GET"] )
def despliegaDashboard():
    if 'nombre' in session:
        listaDojos = Dojo.get_all()
        return render_template("dojosshow.html", dojos=listaDojos )
    else:
        return redirect( '/' )

@app.route('/create/dojo',methods=['POST'])
def crear_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def mostrar_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo=Dojo.obtener_id(data))








