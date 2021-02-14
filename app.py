from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
import models
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from flask_sqlalchemy import SQLAlchemy
from db import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # to indicate that the db is in the root folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # to turn off Flask modeification tracker to use SQLAlchemy mod. tracker which is better (mod tracker is used to monitor changes of object)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app

app.secret_key = 'secret' # hide if the code is public
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) #/auth

db.init_app(app) 

api.add_resource(Item, '/item/<string:name>') # define how it'll be called and parameter 'name' goes to the method (Item class) # http://127.0.0.1:5000/item/Rolf
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register') # UserRegister will be called when 'post' called the end point


if __name__ == '__main__': # so it is executed only if this file is runs, not when it's imported 
    app.run(debug=True)  