from flask import render_template,redirect,session,request, flash
from recetas_app import app
from recetas_app.modelos.recetas import Recipe
from recetas_app.modelos.usuarios import User


@app.route('/receta/<int:id>')
def mostrar_receta(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("view.html",recipe=Recipe.obtener_id(data),user=User.obtener_id(user_data))


@app.route('/nueva/receta')    #Para añadir nueva receta y redigirme a add
def nueva_receta():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('add.html',user=User.obtener_id(data))

@app.route('/crear/receta',methods=['POST'])  #Creo mi nueva receta, validando datos
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/nueva/receta')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "ingredients": request.form["ingredients"],
        "time": int(request.form["time"]),
        "created_at": request.form["created_at"],
        "user_id": session["user_id"]
    }
    Recipe.save(data)
    return redirect('/dashboard')

@app.route( '/receta/remover/<int:id>',methods=['GET'])  #Elimino recetas
def eliminarReceta(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id": id
    }
    Recipe.eliminarRecipe( data )
    #print (resultado) #Por si deseo crear otra variable
    return redirect( '/dashboard' )


@app.route('/actualizar/receta',methods=['POST'])  #Actualizar recetas
def actualizar_receta():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/nueva/receta')
    data = {
        "id": request.form["id"],
        "name": request.form["name"],
        "description": request.form["description"],
        "ingredients": request.form["ingredients"],
        "time": int(request.form["time"])
    }

    Recipe.editarRecipe(data)
    return redirect('/dashboard')


@app.route('/editar/receta/<int:id>')  #Edito recetas
def editar_receta(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit.html",edit=Recipe.obtener_id(data),user=User.obtener_id(user_data))



