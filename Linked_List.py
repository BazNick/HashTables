from Node_class import Node


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, new_value):
        self._head = new_value

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, new_value):
        self._tail = new_value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_value):
        self._size = new_value

    def __len__(self):
        return self.size

    def create_list(self, element):
        node = Node(element, None)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next_node = node
            self.tail = node
        self.size += 1

    def insert_in_order(self, element):
        node = Node(element, None)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            temp = self.head
            if temp.next_node is None:
                if temp.get_element > element:
                    self.head = node
                    node.next_node = self.tail
                else:
                    temp.next_node = node
                    self.tail = node
            else:
                temp_p = temp
                while temp is not None and temp.get_element < element:
                    temp_p = temp
                    temp = temp.next_node
                if temp is self.head:
                    node.next_node = temp
                    self.head = node
                else:
                    node.next_node = temp_p.next_node
                    temp_p.next_node = node
        self.size += 1

    def search_element(self, element):
        temp = self.head
        while temp is not None:
            if element == temp.get_element:
                print('Element is found!')
                return
            else:
                temp = temp.next_node
        print('Element is not found in the List')

    def remove_element(self, element):
        temp = self.head
        temp_p = None
        while temp is not None:
            if element == temp.get_element:
                if temp is self.head:
                    self.head = temp.next_node
                    temp.next_node = None
                    print(f'Element {element} was deleted from the List')
                    self.size -= 1
                    return self.head
                elif temp is self.tail:
                    temp_p.next_node = None
                    self.tail = temp_p
                    print(f'Element {element} was deleted from the List')
                    self.size -= 1
                    return self.tail
                else:
                    temp_p.next_node = temp.next_node
                    temp.next_node = None
                    print(f'Element {element} was deleted from the List')
                    self.size -= 1
                    temp = None
                    return temp
            else:
                temp_p = temp
                temp = temp.next_node
        print('Element is not found in the List')
        return

    def show_elements(self):
        temp = self.head
        while temp is not None:
            print(temp.get_element, end='-->')
            temp = temp.next_node
