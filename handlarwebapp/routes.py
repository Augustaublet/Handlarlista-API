from importlib.metadata import requires
from flask_restful import Resource, abort, reqparse
from handlarwebapp.models import Shoppinglist, Listitem, listItemsInJson, listTitleInJson
from handlarwebapp import db
import json
from flask import jsonify

SECRETKEY = "mklsUgFnJ2AaFGeWz-RjjQ"

def abort_if_list_id_does_not_exist(list_id):
    exists = db.session.query(Shoppinglist.id).filter_by(id=list_id).first() is not None
    if exists == None:
        abort(404, message="Shoppinglist with id {} doesn't exist".format(list_id))

list_parser = reqparse.RequestParser()
item_parser = reqparse.RequestParser()
list_parser.add_argument("newListTitle", required=True, help= "ListTitle kan inte vara blank")
item_parser.add_argument("newItemName",  required=True, help="itemName kan inte vara blank")

class ShoppingListsResorce(Resource):
    # returnerar alla listor i json (listtitle, id)
    def get(self):
        return listTitleInJson()  

    # lägget till en ny lista med "newListTitle" 
    # och returnerar json med alla listor(listTitle, id)
    def post(self):
        args = list_parser.parse_args()
        db.session.add(Shoppinglist(listTitle=args["newListTitle"]))
        db.session.commit()

        return listTitleInJson()  

    def delete(self, list_id):
        db.session.delete(Shoppinglist.query.get(list_id))
        db.session.commit()
        return listTitleInJson() 


class ListItemResorce(Resource):
    def get(self,list_id):
        return listItemsInJson(list_id)

    def post(self, list_id):
        args = item_parser.parse_args()
        db.session.add(Listitem(itemName=args["newItemName"], shoppinglist_id=list_id))
        db.session.commit()
        return listItemsInJson(list_id)
    
    def put(self,list_id,item_id):
        
        pass

    def delete(self,list_id,item_id):
        db.session.delete(Listitem.query.get(item_id))
        db.session.commit()
        return listItemsInJson(list_id)

