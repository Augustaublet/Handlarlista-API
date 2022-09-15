
from classes import *
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# testing
sl = ShoppingList("My Shopping List")
sl.add_item("mjölk")
sl.add_item("smör")
sl.add_item("meritMjölk")
sl.add_item("potatis")


# print("After delete: ")
# sl.delete_item_by_id(1)

# print(sl.itemsListToJson())


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", data=sl)


@app.route("/api/shoppingList", methods=["GET"])
def get_Items():
    return sl.itemsListToJson()


@app.route("/api/shoppingList", methods=["POST"])
def add_Item():
    # if not request.json or not 'title' in request.json:
    #     return "ooups 404 error"
    sl.add_item(request.json["title"])
    return sl.itemsListToJson()


@app.route("/api/shoppingList/<int:item_id>", methods=["PUT"])
def update_Item(item_id):
    sl.update_by_id(str(item_id), request.json["title"], request.json["done"])
    return sl.itemsListToJson()


@app.route("/api/shoppingList/<int:item_id>", methods=["DELETE"])
def remove_Item(item_id):
    sl.remove_item_by_id(str(item_id))
    return sl.itemsListToJson()


if __name__ == "__main__":
    app.run()
