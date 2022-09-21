import secrets
import json


class Item:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.done = False

    def isDone(self, bool):
        self.done = bool

    def update_name(self, new_name):
        self.title = new_name


class ShoppingList(Item):
    def __init__(self, listTitle, listID):
        self.listTitle = listTitle
        self.items = []
        self.ITEM_ID = 0
        self.listID = listID

    def get_list_name(self):
        return self.listTitle

    def add_item(self, title):
        id = self.ITEM_ID
        self.ITEM_ID += 1
        i = Item(str(id), title)
        self.items.append(i)

    def update_by_id(self, id, new_name, newStatus):
        for item in self.items:
            if item.id == id:
                item.update_name(new_name)
                item.isDone(newStatus)

    def remove_item_by_id(self, id):
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
            print("title =", item.title)
            print("is taken= ", item.taken)
            print()

    def itemsListToJson(self):
        return json.dumps(self.items, default=lambda o: o.__dict__, ensure_ascii=False,
                          sort_keys=True, indent=4)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False,
                          sort_keys=True, indent=4)
    
    def titleAndListIDtoJson(self):
        return {"listTitle":self.listTitle, "ListID":self.listID}

def generateListID():
    temp = secrets.token_urlsafe(8)
    print(temp)
    return temp



# Kanske får ta det senare

# class User(ShoppingList):
#     def __init__(self, userName):
#         self.userName = userName
#         self.shopingLists = []

#     def add_new_shoppingList(self, title):
#         self.shopingLists.append(ShoppingList(title))

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
