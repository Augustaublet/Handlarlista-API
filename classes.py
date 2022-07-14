from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import json


class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.taken = False

    def is_taken(self, bool):
        self.taken = bool

    def update_name(self, new_name):
        self.name = new_name


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
                item.is_taken(True)

    def update_name_by_id(self, id, new_name):
        for item in self.items:
            if item.id == id:
                item.update_name(new_name)

    def delete_item_by_id(self, id):
        for item in self.items:
            if item.id == id:
                self.items.remove(item)

    def delete_items_if_taken(self):
        for item in self.items:
            if item.taken == True:
                print(item.taken)
                self.items.remove(item)

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


# sl = ShoppingList("My Shopping List")
# sl.add_item("mjölk")
# sl.add_item("smör")
# sl.add_item("meritMjölk")
# sl.add_item("potatis")
# sl.take_item(3)
# sl.take_item(1)
# sl.print_items()

# print("---------After delete: --------\n")
# sl.delete_items_if_taken()

# sl.print_items()
