from program import *
from invertedIndex import *


if __name__ == "__main__":

    # Problem 1: make a db and write all the data in that file
    # p = Program()
    # p.execute()

    # Problem 2: make an InvertedIndex 
    ii = InvertedIndex()
    ii.makeHashTable()
    print(ii.get("mathematics"))
    print(ii.get("lorem"))
    print(ii.get("an"))
    print(ii.get("science"))
    

    