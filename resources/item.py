from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sys
sys.path.append(r'/Users/vasilisa/Desktop/flask/section6/code')
from models.item import ItemModel


"""Resources are what users can sask an API for - external representation of an entity """

class Item(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('price',
        type=float,
        required=True,
        help="Field 'price' cannot be left blank and has to be a number!")
  
  parser.add_argument('store_id',
        type=float,
        required=True,
        help="Field 'store_id' cannot be left blank and has to be an integer!")

  def get(self, name):
    item = ItemModel.find_by_name(name)
    if item:
        return item.json() 
    return {'message':'Item not found'}, 404 # gives 404 status instead of 200

  #@jwt_required()
  def post(self, name):
    if ItemModel.find_by_name(name): # same as Item.find_by_name(name)
      return {'message': f'item {name} already exists'}, 400 # 400 - bad request 
    
    data = Item.parser.parse_args() # check for required arguments 
    item = ItemModel(name, data['price'], data['store_id'])
    try:
        item.save_to_db()
    except:
        return {"message":"An error occured inserting the data"}, 500 # internal server error, not user's fault 
    return item.json(), 201
    
  @jwt_required()
  def delete(self, name):
    item = ItemModel.find_by_name(name)
    if item is None: # same as Item.find_by_name(name)
      return {'message': f'item {name} not found'}, 400 # 400 - bad request 
    
    item.delete_from_db()
    return {'message': f'Item {name} deleted'}

  #@jwt_required()
  def put(self, name):
    data = Item.parser.parse_args()
    item = ItemModel.find_by_name(name)

    if item is None:
      item = ItemModel(name, **data)# ** data = data['price'], data['store_id']
    else:
      item.price = data['price']
      item.store_id = data['store_id']
    item.save_to_db()
    return item.json()
    

class ItemList(Resource):
    def get(self):
      return {'item': [item.json() for item in ItemModel.query.all()]}