from . import db
from flask import jsonify
class Listitem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(50), nullable=False)
    itemIsDone = db.Column(db.Boolean, unique=False, default=False) 
    shoppinglist_id = db.Column(db.Integer, db.ForeignKey('shoppinglist.id'))

class Shoppinglist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listTitle = db.Column(db.String(50), nullable=False)   
    items = db.relationship('Listitem')
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    sharedWith = db.relationship('user')
    

    # detta behöver testas. Oklar över relationerna få det är en åt varje håll...
class User(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50),nullable=False)
    myLists = db.relationship('Shoppinglist')
    sharedWithMe = db.Column(db.Integer, db.ForeignKey('shoppinglist.id'))





def listTitleInJson():
    queryresult= Shoppinglist.query.all()
    jsonlista = []
    for lista in queryresult:
        jsonlista.append({"listTitle":lista.listTitle, "id":lista.id})
    return jsonify(jsonlista)

def listItemsInJson(list_id):
    queryresult = Listitem.query.filter_by(shoppinglist_id=list_id)
    jsonlista= []
    for item in queryresult:
        jsonlista.append({"id":item.id,"itemName":item.itemName,"itemIsDone":item.itemIsDone})
    return jsonify(jsonlista)
