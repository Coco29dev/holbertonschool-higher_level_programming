#!/usr/bin/python3

class VerboseList(list):
    def append(self, item):
        print(f"Added {[item]} to the list.")
        super().append(item)

    def extend(self, x):
        new_x = len(x)
        print(f"Extended the list with {[new_x]} item.")
        super().extend(x)

    def remove(self, item):
        print(f"Added {[item]} to the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped {[item]} from the list.")
        super().pop(index)
