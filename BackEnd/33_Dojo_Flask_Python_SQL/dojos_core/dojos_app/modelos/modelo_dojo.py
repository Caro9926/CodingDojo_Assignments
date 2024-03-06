from dojos_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def obtener_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('esquema_dojos_ninjas').query_db(query)
        listadojos = []
        for dojo in results:
            listadojos.append( cls( dojo["id"], dojo["nombre"]) )
        return listadojos


    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"

        # comes back as the new row id
        result = connectToMySQL('esquema_dojos_ninjas').query_db(query,data)
        return result

    @classmethod
    def obtener_id(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('esquema_dojo_ninjas').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for r in results: #coloco las variables con el que hago merge
            n = {
                'id': r['ninjas.id'],
                'first_name': r['first_name'],
                'last_name': r['last_name'],
                'age': r['age'],
                'created_at': r['ninjas.created_at'],
                'updated_at': r['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(n) )
        return dojo
       


    def existeDojo( id_dojo, listadojos):
        for i in range( 0, len(listadojos)):
            if listadojos[i].id == id_dojo:
                return i
        return -1


