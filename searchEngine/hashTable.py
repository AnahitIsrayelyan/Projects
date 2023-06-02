from singlyLinkedList import *


class HashTable:
    def __init__(self) -> None:
        self.capacity = 1001
        self.array = [None] * self.capacity

    def printTable(self):
        for node in self.array:
            if node is not None:
                print(node)
                
    def hashFunction(self, key: str) -> int:
        summ = 0
        for char in key:
            summ += ord(char)
        return (summ % self.capacity)

    def set(self, key: str, value):
        hashValue = self.hashFunction(key)
        if self.array[hashValue] is None:
            self.array[hashValue] = LinkedList()
            self.array[hashValue].push_front(Node(key, [str(value)]))
        else:
            head = self.array[hashValue].head
            while head:
                if head.key == key:
                    if str(value) not in head.value:
                        head.value.append(str(value))
                    break
                head = head.next

    def get(self, key: str) -> int:
        elem = self.array[self.hashFunction(key)]
        if elem is not None:
            head = elem.head
            while head:
                if head.key == key:
                    res = " -> ".join(head.value)
                    return f"{head.key}: {res}"
                head = head.next
        return "Not such an element."
    
    # def set(self, key: str, value):
    #     hashValue = self.hashFunction(key)
    #     if self.array[hashValue] is None:
    #         self.array[hashValue] = LinkedList()
    #     self.array[hashValue].push_front(Node(key, value))

    # def get(self, key: str) -> int:
    #     hashValue = self.hashFunction(key)
    #     return self.array[hashValue].find(key) if self.array[hashValue] else None
    
    def remove(self, key):
        hashValue = self.hashFunction(key)
        self.array[hashValue].remove(key)


if __name__ == "__main__":
    tab = HashTable()
    tab.set('Anahit', "1.txt")
    tab.set('Anahit', "2.txt")
    tab.set('Anahit', "2.txt")
    tab.set('Anahit', "2.txt")
    tab.set('Lyusi', "1.txt")
    tab.set('Samvel', "2.txt")

    print(tab.get("Anahit"))

    # tab.printTable()

    # print(tab.get('Lyusi'))
    # print(tab.get('Samvel'))
    # print(tab.get('Anahit'))
    
    # print(tab.hashFunction('Lyusi'))
    # print(tab.hashFunction('Samvel'))
    # print(tab.hashFunction('Anahit'))
    
    # print(tab.array[tab.hashFunction('Lyusi')])
    # tab.remove('Lyusi')
    # print(tab.array[tab.hashFunction('Lyusi')])
