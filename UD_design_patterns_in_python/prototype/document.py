"""Document class that implements the prototype interface."""

import copy
from interface_prototype import IPrototype


class Document(IPrototype):  # pylint: disable=too-few-public-methods
    """A concrete class that implement the prototype interface."""

    def __init__(self, name, doc_list):
        self.name = name
        self.list = doc_list

    def clone(self, mode):
        """This method uses different techniques to make a copy."""
        if mode == 1:
            # this results in a 1 level deep copy of the document
            # this basically creates another name for teh same object and points to the same place
            # this is sort of a pseudo copy because it does not really copy anything, it just
            # creates a new pointer to teh same object
            doc_list = self.list
        elif mode == 2:
            # result in a 2 level deep shallow copy of the document
            # this creates new references for teh 1st level list elements
            doc_list = self.list.copy()
        elif mode == 3:
            # this mode creates a recursive deep copy
            doc_list = copy.deepcopy(self.list)
        else:
            doc_list = None

        return type(self)(
            self.name,
            doc_list
        )

    def __str__(self):
        """Overriding the default __str__ method that is used when print() is used on the object."""
        return f'id of object:{id(self)}\t' \
               f'id of list:{id(self.list)}\t' \
               f'name={self.name}\tlist={self.list}'
