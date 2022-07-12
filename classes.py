import json


class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.taken = False


class ShoppingList(Item):
    def __init__(self, listName):
        self.listName = listName
        self.items = []

    def add_item(self, name):
        id = len(self.items)
        i = Item(id, name)
        self.items.append(i)

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
