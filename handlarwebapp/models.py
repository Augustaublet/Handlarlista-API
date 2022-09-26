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
