from flask_restful import Resource, abort, reqparse
from handlarwebapp.models import Shoppinglist, Listitem, listItemsInJson, listTitleInJson
from handlarwebapp import db


# SECRETKEY = "mklsUgFnJ2AaFGeWz-RjjQ"

# def abort_if_list_id_does_not_exist(list_id):
#     exists = db.session.query(Shoppinglist.id).filter_by(id=list_id).first() is not None
#     if exists == None:
#         abort(404, message="Shoppinglist with id {} doesn't exist".format(list_id))

list_parser = reqparse.RequestParser()
new_item_parser = reqparse.RequestParser()
item_parser = reqparse.RequestParser()

list_parser.add_argument("newListTitle", required=True, help= "newListTitle kan inte vara blank")
item_parser.add_argument("newItemName")
item_parser.add_argument("itemIsDone", type=bool)
item_parser.add_argument("deleteAllDone", type= bool, help= "this command neads to be a bool")


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
    
    def put(self,list_id):
        args = list_parser.parse_args()
        list_to_update = Shoppinglist.query.get(list_id)
        list_to_update.listTitle = args["newListTitle"]
        db.session.commit()
        return listTitleInJson() 
    # tar bort en lista men hjälp av list_id
    def delete(self, list_id):
        db.session.delete(Shoppinglist.query.get(list_id))
        db.session.commit()
        return listTitleInJson() 


class ListItemResorce(Resource):
    # returnerar en lista efter list_id i json itemName, id, itemIsDone
    def get(self,list_id):
        return listItemsInJson(list_id)
    # lägga till item i listan(kräver newItemName) och 
    # ta bort alla avklarade(itemIsDone) med deleteAllDone=true
    def post(self, list_id):
        args = item_parser.parse_args()
        if args.deleteAllDone == True:          # kollar om deleteAllDone existerar
            Listitem.query.filter_by(shoppinglist_id=list_id, itemIsDone = True).delete()
            db.session.commit()
            return listItemsInJson(list_id)
        else:
            db.session.add(Listitem(itemName=args["newItemName"], shoppinglist_id=list_id))
            db.session.commit()
        return listItemsInJson(list_id)
    
    #uppdaterar item med newItemName och itemIsDone
    def put(self,list_id,item_id):
        args = item_parser.parse_args()
        itemToUpdate = Listitem.query.get(item_id)
        itemToUpdate.itemName = args["newItemName"]
        itemToUpdate.itemIsDone = args["itemIsDone"]
        db.session.commit()
        return listItemsInJson(list_id)

    # tar bort ett item efte item_id. list_id krävs endast för att 
    # returnera rätt lista(också lättare med path)
    def delete(self,list_id,item_id):
        db.session.delete(Listitem.query.get(item_id))
        db.session.commit()
        return listItemsInJson(list_id)

