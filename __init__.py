
from classes import *
from flask import Flask, render_template, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# testing

ListOfShopplinglists = []
ListOfShopplinglists.append(ShoppingList(
    "My Shopping List Test", "mklsUgFnJ2AaFGeWz-RjjQ"))
ListOfShopplinglists[0].add_item("mjölk")
ListOfShopplinglists[0].add_item("smör")
ListOfShopplinglists[0].add_item("meritMjölk")
ListOfShopplinglists[0].add_item("potatis")


# print("After delete: ")
# sl.delete_item_by_id(1)

# print(sl.itemsListToJson())


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", data=sl)


@app.route("/api/shoppingList/register", methods=["POST"])
def register():
    newKey = generateKey()
    # change first newKey to request.json["title"]
    newListItem = ShoppingList(newKey, newKey)
    ListOfShopplinglists.append(newListItem)
    return {"title": newListItem.title, "apiKey": newListItem.apiKey}


@app.route("/api/shoppingList", methods=["GET"])
def get_Items():
    list = getListClass(request.args.get("key"))
    return list.itemsListToJson()


@app.route("/api/shoppingList", methods=["POST"])
def add_Item():
    if not request.json or not 'title' in request.json:
        abort(404)
    list = getListClass(request.args.get("key"))
    list.add_item(request.json["title"])
    return list.itemsListToJson()


@app.route("/api/shoppingList/<int:item_id>", methods=["PUT"])
def update_Item(item_id):
    list = getListClass(request.args.get("key"))

    list.update_by_id(
        str(item_id), request.json["title"], request.json["done"])
    return list.itemsListToJson()


@app.route("/api/shoppingList/<int:item_id>", methods=["DELETE"])
def remove_Item(item_id):
    list = getListClass(request.args.get("key"))
    print(item_id)
    list.remove_item_by_id(str(item_id))
    return list.itemsListToJson()


def getListClass(key):
    for list in ListOfShopplinglists:
        if list.apiKey == key:
            return list


if __name__ == "__main__":
    app.run()
