from flask_sqlalchemy import SQLAlchemy
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from db import db 
print(parentdir)
class ItemModel(db.Model):
    __tablename__ = 'items' # tell sqlalchemny which table to use and what columns are there 
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80)) # 8- char max to limit lenght of the name 
    price = db.Column(db.Float(precision=2))
    
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self): # to return a json representation of a model 
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # select * from table_name where name=name limit 1

    def save_to_db(self): # either create or update
        # directly insert object into a db
        db.session.add(self) # session are the objects that we insert 
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

        
   


    