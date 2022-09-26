from importlib.metadata import requires
from flask_restful import Resource, abort, reqparse
from handlarwebapp.models import Shoppinglist, Listitem, listInJson
from handlarwebapp import db
import json
from flask import jsonify

SECRETKEY = "mklsUgFnJ2AaFGeWz-RjjQ"

def abort_if_list_id_does_not_exist(list_id):
    exists = db.session.query(Shoppinglist.id).filter_by(id=list_id).first() is not None
    if exists == None:
        abort(404, message="Shoppinglist with id {} doesn't exist".format(list_id))

parser = reqparse.RequestParser()
parser.add_argument("newListTitle", required=True, help= "ListTitle kan inte vara blank")

class ShoppingListsResorce(Resource):
    # returnerar alla listor i json (listtitle, id)
    def get(self):
        return listInJson(Shoppinglist.query.all())  

    # lägget till en ny lista med "newListTitle" 
    # och returnerar json med alla listor(listTitle, id)
    def post(self):
        args = parser.parse_args()
        newListTitle = args["newListTitle"]
        db.session.add(Shoppinglist(listTitle=newListTitle))
        db.session.commit()

        return listInJson(Shoppinglist.query.all())  

    def delete(self, list_id):
        db.session.delete(Shoppinglist.query.get(list_id))
        db.session.commit()
        return listInJson(Shoppinglist.query.all()) 


class ListItemResorce(Resource):
    def get(self,list_id):
        pass