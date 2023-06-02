from hashTable import HashTable
from singlyLinkedList import *
from wordAndText import *

files = {
    '1.txt': 1, 
    '2.txt': 2
    }

# 1. make a hashTable
# 2. Text.execute for all files, use a loop
# 3. set all self._word from Text objects self._words in the hashTable
class InvertedIndex:
    def __init__(self) -> None:
        self._table = HashTable()

    def makeHashTable(self):
        for filename in files.keys():
            # print()
            file = Text(filename)
            file.executet()
            for word in file._words:
                self._table.set(word.get(), filename)

    def get(self, key):
        return self._table.get(key) 



if __name__ == "__main__":
    tab = InvertedIndex()
    tab.makeHashTable()
    print(tab.get("mathematics"))
