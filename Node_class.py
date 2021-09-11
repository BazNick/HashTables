class Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

    @property
    def get_element(self):
        return self._element

    @property
    def next_node(self):
        return self._next

    @next_node.setter
    def next_node(self, new_value):
        self._next = new_value
