from Linked_List import LinkedList


class HashChain:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hashtable = [0] * self.table_size
        for i in range(len(self.hashtable)):
            self.hashtable[i] = LinkedList()

    def __len__(self):
        return len(self.hashtable)

    def hashcode(self, key):
        return key % self.table_size

    def insert(self, element):
        index = self.hashcode(element)
        self.hashtable[index].insert_in_order(element)

    def search_value(self, key):
        index = self.hashcode(key)
        return self.hashtable[index].search_element(key)

    def remove_value(self, key):
        index = self.hashcode(key)
        return self.hashtable[index].remove_element(key)

    def display(self):
        for j in range(self.table_size):
            print('[', j, ']', end=' ')
            self.hashtable[j].show_elements()
            print()
