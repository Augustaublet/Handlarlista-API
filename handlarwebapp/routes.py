from flask_restful import Resource
from .models import ShoppingList, ListItem
from handlarwebapp import db
import json

SECRETKEY = "mklsUgFnJ2AaFGeWz-RjjQ"




class GetShoppingLists(Resource):
    def get(self):
        return {"hello":"world"}


