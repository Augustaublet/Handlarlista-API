import re
from classes import *
from flask import Flask, render_template, request

app = Flask(__name__)


# testing
sl = ShoppingList("My Shopping List")
sl.add_item("mjölk")
sl.add_item("smör")
sl.add_item("meritMjölk")
sl.add_item("potatis")
sl.take_item_by_id(3)
sl.take_item_by_id(1)

# print("After delete: ")
# sl.delete_item_by_id(1)

print(sl.toJSON())


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", data=sl)


@app.route("/api/shoppingList", methods=["GET"])
def api():
    if "add_item" in request.args:
        # get "add_item", "name"
        sl.add_item(request.args.get("name"))
    if "update_item_name" in request.args:
        # get "update_item_name", "id", new_name
        sl.update_name_by_id(request.args.get(
            "id"), request.args.get("new_name"))
    if "take_item" in request.args:
        # get "take_item", "id"
        sl.take_item_by_id(request.args.get("id"))
    if "delete_by_id" in request.args:
        # get "delete_by_id", "id"
        sl.delete_item_by_id(request.args.get("id"))
    if "delete_if_taken" in request.args:
        # get "delete_if_taken"
        sl.delete_items_if_taken()
    # behöver fundera på vad varje funktion skall returnera?
    # Skall allt returneras igen eller bara det som är nödvändigt?
    print(sl.toJSON)
    return sl.toJSON()


if __name__ == "__main__":
    app.run(debug=True)
