from classes import *
from flask import Flask, render_template

app = Flask(__name__)

# testing
sl = ShoppingList("My Shopping List")
sl.add_item("mjölk")
sl.add_item("smör")
sl.take_item(1)

# sl.print_items()

print(sl.toJSON())


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", data=sl)


@app.route("/api/shopingList", methods=["GET"])
def api():
    return sl.toJSON()


if __name__ == "__main__":
    app.run(debug=True)
