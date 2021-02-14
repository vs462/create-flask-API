import sqlite3
from flask_sqlalchemy import SQLAlchemy
import os, sys
from db import db 

""" models are the internal representation, how we manipulate the date"""
class UserModel(db.Model):
    __tablename__ = 'users' # tell sqlalchemny which table to use and what columns are there 
    
    id = db.Column(db.Integer, primary_key = True) # auto incrementing -> self.id is automatically generated 
    username = db.Column(db.String(80)) # 8- char max to limit lenght of the name 
    password = db.Column(db.String(80))
    
    def save_to_db(self):# either create or update
        # directly insert object into a db
        db.session.add(self) # session are the objects that we insert 
        db.session.commit()    

    def __init__(self, username, password):
        self.username = username # name should match the columns, anything else won't get to the db 
        self.password = password 

    @classmethod # to not hardcode the name of the class within the method
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=id).first()

