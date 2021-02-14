import sqlite3
from flask_restful import Resource, reqparse 
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from models.user import UserModel


class UserRegister(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser() # enable to add and parse multiple arguments. It will parse through the json reques to make sure the required fields are there 
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args() # use the parser to get payload

        if UserModel.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400

        user=UserModel(**data) # = (data['username'], data['password']) 
        user.save_to_db()

        return {"message": "User created successfully."}, 201