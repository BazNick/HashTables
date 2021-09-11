from Hash_Table import HashChain

if __name__ == '__main__':
    hash_table = HashChain(10)

    hash_table.insert(45)
    hash_table.insert(23)
    hash_table.insert(10)
    hash_table.insert(89)
    hash_table.insert(56)
    hash_table.insert(76)

    hash_table.display()
    hash_table.search_value(89)
