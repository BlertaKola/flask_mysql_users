#here we use oop classes
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name = 'users_db'
    def __init__(self,data):
        self.id = data['id'],
        self.first_name = data['first_name'], 
        self.last_name = data['last_name'],
        self.email = data['email'], 
        self.created_at = data['created_at'], 
        self.updated_at = data['updated_at'] 


    @classmethod
    def getAllUsers(cls):
        query = 'SELECT * FROM users;'
        result = connectToMySQL(cls.db_name).query_db(query)
        return result


    @classmethod
    def add_user(cls,data):
        query = 'INSERT INTO users (first_name, last_name, email) VALUES ( %(first_name)s, %(last_name)s, %(email)s );'
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def getUserById(cls,data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result[0]

    @classmethod
    def updateUser(cls,data):
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;' 
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    

    @classmethod
    def deleteUser(cls,data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        return connectToMySQL(cls.db_name).query_db(query,data)
