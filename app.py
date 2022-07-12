from classes import *
from flask import Flask, render_template

app = Flask(__name__)

# testing
sl = ShoppingList("My Shopping List")
sl.add_item("mjölk")
sl.add_item("smör")

sl.print_items()

print(sl.toJSON())


@app.route("/", methods=["GET"])
def home():
    pass


@app.route("/api/shopingList", methods=["GET"])
def api():
    return sl.toJSON()


if __name__ == "__main__":
    app.run(debug=True)
