from . import db

class Listitem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(50), nullable=False)
    itemIsDone = db.Column(db.Boolean, unique=False, default=False) 
    shopinglist_id = db.Column(db.Integer, db.ForeignKey('shoppinglist.id'))
    # mylist = db.relationship("shoppinglist", 
        # backref="shoppinglist", lazy=True)

class Shoppinglist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listTitle = db.Column(db.String(50), nullable=False)   
    # items = db.Column(db.Integer, 
    #     db.ForeignKey('shoppinglist.id'), nullable=False) 
    items = db.relationship('Listitem')