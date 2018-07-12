from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self,name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item':None}, 404
    
    def post(self,name):
        item = {'name':name, 'price':12.00}
        items.append(item)
        return item,201  #201 status code for insertion successful (Created)
        #202 for showing clients that we will create the object but not now so your request is accepted

api.add_resource(Item,'/item/<string:name>')


app.run(port=5000)