import random

from Hash_Table import HashChain

random.seed(1)


def create():
    hash_table = HashChain(10)
    for i in range(10):
        hash_table.insert(random.randint(10, 100))
    return len(hash_table)


def search():
    hash_table = HashChain(10)
    for i in range(10):
        hash_table.insert(random.randint(10, 100))

    value_in_table = hash_table.search_value(87)
    return value_in_table


def remove():
    hash_table = HashChain(10)
    for i in range(10):
        hash_table.insert(random.randint(10, 100))

    hash_table.remove_value(67)
    value_in_table = hash_table.search_value(67)

    return value_in_table
