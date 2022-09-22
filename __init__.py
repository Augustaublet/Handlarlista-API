
from json import JSONEncoder
from typing import List
from classes import *

from flask import Flask, render_template, request, abort
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

SECRETKEY = "mklsUgFnJ2AaFGeWz-RjjQ"


# testing

ListOfShopplinglists = []
ListOfShopplinglists.append(ShoppingList(
    "HandlarLista", "0v_DQMrr3Qk"))
ListOfShopplinglists[0].add_item("mjölk")
ListOfShopplinglists[0].add_item("smör")
ListOfShopplinglists[0].add_item("meritMjölk")
ListOfShopplinglists[0].add_item("potatis")
ListOfShopplinglists.append(ShoppingList(
    "Att göra lista", "KvSFI95gEtg"))
ListOfShopplinglists[1].add_item("mjölk2")
ListOfShopplinglists[1].add_item("smör2")
ListOfShopplinglists[1].add_item("meritMjölk2")
ListOfShopplinglists[1].add_item("potatis2")

def getListClass(key):
    for list in ListOfShopplinglists:
        if list.listID == key:
            return list


# print("After delete: ")
# sl.delete_item_by_id(1)
templist = getListClass("0v_DQMrr3Qk")
print(templist.itemsListToJson())
for x in ListOfShopplinglists:
        print(x.toJSON())


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/api/shoppingList/register", methods=["POST"])
def register():
    newListID = generateListID()
    # change first newListID to request.json["listTitle"]
    newList = ShoppingList(newListID, newListID)
    ListOfShopplinglists.append(newList)
    return {"listTitle": newList.title, "listID": newListID}


@app.route("/api/allshoppinglists", methods= ["GET"])
def get_all_lists():
    if request.args.get("key") == SECRETKEY:
        listToReturn = []
        for l in ListOfShopplinglists:
            listToReturn.append(l.titleAndListIDtoJson())
        return json.dumps(listToReturn)
    else:
        return []

@app.route("/api/shoppingList", methods=["GET"])
def get_Items():
    list = getListClass(request.args.get("listID"))
    return list.itemsListToJson()


@app.route("/api/shoppingList", methods=["POST"])
def add_Item():
    #if not request.json or not 'title' in request.json:
     #   abort(404)
    list = getListClass(request.args.get("listID"))
    list.add_item(request.json["title"])
    return list.itemsListToJson()


@app.route("/api/shoppingList/<int:item_id>", methods=["PUT"])
def update_Item(item_id):
    list = getListClass(request.args.get("listID"))

    list.update_by_id(
        str(item_id), request.json["title"], request.json["done"])
    return list.itemsListToJson()


@app.route("/api/shoppingList/<int:item_id>", methods=["DELETE"])
def remove_Item(item_id):
    list = getListClass(request.args.get("listID"))
    print(item_id)
    list.remove_item_by_id(str(item_id))
    return list.itemsListToJson()





if __name__ == "__main__":
    app.run(host="192.168.1.137")
