from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import json


class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.taken = False

    def is_taken(self):
        self.taken = True


class ShoppingList(Item):
    def __init__(self, listName):
        self.listName = listName
        self.items = []
        self.ITEM_ID = 0

    def add_item(self, name):
        id = self.ITEM_ID
        self.ITEM_ID += 1
        i = Item(id, name)
        self.items.append(i)

    def take_item(self, id):
        for item in self.items:
            if item.id == id:
                item.is_taken()

    def print_items(self):
        print(self.listName)
        for item in self.items:
            print("id = ", item.id)
            print("name =", item.name)
            print("is taken= ", item.taken)
            print()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False,
                          sort_keys=True, indent=4)

# Kanske får ta det senare

# class User(ShoppingList):
#     def __init__(self, userName):
#         self.userName = userName
#         self.shopingLists = []

#     def add_new_shoppingList(self, name):
#         self.shopingLists.append(ShoppingList(name))

#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__,
#                           sort_keys=True, indent=4)
