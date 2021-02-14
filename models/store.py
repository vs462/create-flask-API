from flask_sqlalchemy import SQLAlchemy
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from db import db 

class StoreModel(db.Model):
    __tablename__ = 'stores' # tell sqlalchemny which table to use and what columns are there 
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80)) # 8- char max to limit lenght of the name 
    
    items=db.relationship('ItemModel', lazy = "dynamic") # flask would go to ItemModel and find the relationship (many to one rel)
    # lazy refers to elf.price.all below. It wouldn't work without '.all' and it wouldn't call the items table unless the def json() is called as it's set to lazy

    def __init__(self, name):
        self.name = name

    def json(self): # to return a json representation of a model 
        return {'name': self.name, 'items':[item.json() for item in self.items.all()]}

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

        
   


    