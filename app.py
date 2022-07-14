from classes import *
from flask import Flask, render_template

app = Flask(__name__)

# testing
sl = ShoppingList("My Shopping List")
sl.add_item("mjölk")
sl.add_item("smör")
sl.add_item("meritMjölk")
sl.add_item("potatis")
sl.take_item(3)
sl.take_item(1)

# print("After delete: ")
# sl.delete_item_by_id(1)

print(sl.toJSON())


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", data=sl)


@app.route("/api/shoppingList", methods=["GET"])
def api():
    return sl.toJSON()


if __name__ == "__main__":
    app.run(debug=True)
