from recetas_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.ingredients = data['ingredients']
        self.time = data['time']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, ingredients, time, user_id) VALUES (%(name)s,%(description)s, %(ingredients)s, %(time)s, %(user_id)s);"

        result = connectToMySQL('esquema_recetas').query_db(query,data)
        return result
     
    @classmethod
    def obtener_receta(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('esquema_recetas').query_db(query)
        recipes = []
        for recetas in results:
            recipes.append( cls(recetas))
        return recipes

  
    @classmethod
    def obtener_id(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL('esquema_recetas').query_db(query,data)
        return cls(results[0])

    @classmethod
    def eliminarRecipe( cls, data ):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        resultado = connectToMySQL( "esquema_recetas" ).query_db( query, data )
        return resultado

    @classmethod
    def obtenerDatosRecipe( cls, data ):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        resultado = connectToMySQL( "esquema_recetas" ).query_db( query, data )
        return resultado
    
    @classmethod
    def editarRecipe( cls, data ):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, ingredients = %(ingredients)s, time = %(time)s WHERE id = %(id)s;"
        resultado = connectToMySQL( "esquema_recetas" ).query_db( query, data )
        return resultado

 
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 4:
            is_valid = False
            flash("Name must be at least 4 characters","recipe")
        if len(recipe['description']) < 8:
            is_valid = False
            flash("Instructions must be at least 8 characters","recipe")
        if len(recipe['ingredients']) < 10:
            is_valid = False
            flash("Description must be at least 10 characters","recipe")
        return is_valid