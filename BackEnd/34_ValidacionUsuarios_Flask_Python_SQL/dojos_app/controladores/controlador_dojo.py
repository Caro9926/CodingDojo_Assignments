from flask import Flask, redirect, session, render_template, request
from dojos_app import app
from dojos_app.modelos.modelo_dojo import Dojo


@app.route( '/', methods=['GET'] )
def despliegaRegistroLogin():
    return render_template( "index.html" )


@app.route('/formulario',methods=['POST'])
def create_dojo():
    #print("AQUI REQUEST FORM", request.form) Imprimo para verificar
    if not Dojo.is_valid(request.form):
        return redirect('/')
    Dojo.save(request.form)
    return redirect('/dashboard')
    


@app.route( '/dashboard', methods=["GET"] )
def despliegaDashboard():
        return render_template( "dashboard.html", usuarios= Dojo.obtener_dojos())


@app.route( '/logout', methods=["GET"] )
def logoutUsuario():
    session.clear()
    return redirect( '/' )