from dojos_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['first_name']
        self.name = data['last_name']
        self.name = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s, %(age)s, %(dojo_id)s);"

        # comes back as the new row id
        result = connectToMySQL('esquema_dojos_ninjas').query_db(query,data)
        return result

  

