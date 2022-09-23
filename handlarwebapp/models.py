from . import db

class ShoppingList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listTitle = db.Column(db.String(50), nullable=False)   
    listItem = db.relationship("ListItem")

class ListItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(50), nullable=False)
    itemIsDone = db.Column(db.Boolean, unique=False, default=False)
    shoppingListID = db.Column(db.Integer, db.ForeignKey('shoppinglist.id'))