#!/usr/bin/python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {[item]} to the list.")

    def extend(self, x):
        new_x = len(x)
        super().extend(x)
        print(f"Extended the list with {[new_x]} item.")

    def remove(self, item):
        print(f"Added {[item]} to the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped {[item]} from the list.")
        super().pop(index)
