
"""
Item class represents an item in a text-based adventure game.
It keeps track of the item's name and can be extended with more attributes and methods as needed.
"""

class Item:
    def __init__(self, name:str)-> None:
        self.name = name
        
    def __str__(self):
        return f"Name: {self.name}"
   
if __name__ == "__main__":
    item = Item("Sample Item")
    print(item)