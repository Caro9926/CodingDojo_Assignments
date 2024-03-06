from flask import Flask, render_template, request, redirect, session
# importar la clase de friend.py
from friend import Friend
app = Flask(__name__)

@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends =friends)

@app.route('/user/new')
def new():
    return render_template("dashboard.html")


@app.route('/user/create', methods=["POST"])
def create_friend():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "em" : request.form["em"]
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    Friend.save(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/dashboard')


@app.route( '/logout', methods=["GET"] )
def logoutUsuario():
    session.clear()
    return redirect( '/' )

            
if __name__ == "__main__":
    app.run(debug=True)