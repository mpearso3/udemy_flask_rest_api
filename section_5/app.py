from flask import Flask, render_template
from flask_restful import Api, Resource

app = Flask (__name__)
api = Api (app)

items = []

class Item (Resource):
  def get (self, name):
    return {'item': next (filter (lambda x: x['name'] == name, items), None)}

  def put (self, name):
    if (next (filter (lambda x: x['name'] == name, items), None) is not None):
      return {'message': 'name already exists in items'} 

    item = {'name': name, 'value': 'random_value'}
    items.append(item)
    return {'item': item}

class ItemList (Resource):
  def get (self):
    return {'items': items} 

api.add_resource (Item, '/item/<string:name>')
api.add_resource (ItemList, '/items')

app.run (host="0.0.0.0", port=5000, debug=True)
