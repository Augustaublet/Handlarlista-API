import email
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
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sharedWith = db.relationship('user')
    

    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50),nullable=False)
    myLists = db.relationship('Shoppinglist')
    sharedWithMe = db.Column(db.Integer, db.ForeignKey('shoppinglist.id'))
    email = db.Column(db.String(80))
    devices = db.relationship('DeviceModel', back_popilates='user')

class DeviceModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    device_name = db.Column(db.String(80))
    device_key = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='devices')





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
