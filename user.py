from mysqlconnection import connectToMySQL
from flask import flash
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['name']
        self.last_name = data['location']
        self.email = data['language']
        self.email = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['message']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        return is_valid

