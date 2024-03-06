from flask import Flask
from dojos_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['ubication']
        self.idioma = data['idioma']
        self.comment = data['comentario']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def obtener_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('esquema_dojos_ninjas2').query_db(query) # retorna Lista de diccionarios
        print("OBTERNER TODAS DOJOS", results) #Puedo ver si está jalando o no
        listadojos = [] # lista de objetos
        for dojo in results:
            listadojos.append( cls( dojo) ) #Crear objetos 
        return listadojos
    
    
    @classmethod
    def save(cls, data): #Debido a que empleo request form, debo tomar los valores que asigno en el HTMl
        query = "INSERT INTO dojos (name, ubication, idioma, comentario, created_at, updated_at) VALUES (%(nombre)s,%(location)s, %(favorito)s, %(comments)s, NOW(), NOW());"

        # comes back as the new row id
        result = connectToMySQL('esquema_dojos_ninjas2').query_db(query,data)
        print("VERIFICAR SI SE CREA REGISTRO", result)
        return result

    @staticmethod
    def is_valid(dojos):
        is_valid = True
        if len(dojos['nombre']) < 3:
            flash("El nombre debe tener al menos tres caracteres")
            is_valid = False     
        if len(dojos['location']) < 1:
            flash("Debes escoger una ubicación del dojo")
            is_valid = False
        if len(dojos['favorito']) < 1:
            flash("Debes escoger tu lenguaje favorito")
            is_valid = False   
        if len(dojos['comments']) < 2:
            flash("Un comentario debe tener al menos ocho caracteres")
            is_valid = False
        return is_valid