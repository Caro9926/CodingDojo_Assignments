#Esta es una adaptación del formulario visto en clases de Coding Dojo
from flask import Flask, render_template, request, redirect, session

app = Flask( __name__ )
app.secret_key = "usuariocore"

listaUsuarios = []

@app.route( '/', methods=['GET'] )
def despliegaRegistroLogin():
    return render_template( "index.html" )

@app.route( '/dashboard', methods=["GET"] )
def despliegaDashboard():
    if 'nombre' in session:
        return render_template( "dashboard.html", usuarios=listaUsuarios )
    else:
        return redirect( '/' )

@app.route( '/registroUsuario', methods=["POST"] )
def registrarUsuario():
    nuevoUsuario = {
        "nombre" : request.form["nombre"],
        "location" : request.form["location"],
        "favorito" : request.form["favorito"],
        "comments" : request.form["comments"]
    }
    session["nombre"] = request.form["nombre"]
    session["location"] = request.form["location"]
    session["favorito"] = request.form["favorito"]
    session["comments"] = request.form["comments"]
    listaUsuarios.append( nuevoUsuario )
    return redirect( '/dashboard' )



@app.route( '/logout', methods=["GET"] )
def logoutUsuario():
    session.clear()
    return redirect( '/' )

if __name__ == "__main__":
    app.run( debug = True )