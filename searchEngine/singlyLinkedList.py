class Node:
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.key) + ":" + str(node.value))
            node = node.next
        # nodes.append("None")
        return "->".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def push_front(self, new_node: Node):
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, target_value, new_node: Node):
        if self.head is None:
            print("Is empty.")
            return
        
        for node in self:
            if node.key == target_value:
                new_node.next = node.next
                node.next = new_node
                # print(target_value, "node is inserted.")
                return
            
        # print("There is no such a value.")

    def remove(self, target_value):
        if self.head is None:
            # print("Is empty")
            return
        
        if self.head.key == target_value:
            self.head = self.head.next
            return
        
        ptr_to_prev = self.head
        for node in self:
            if node.key == target_value:
                ptr_to_prev.next = node.next
                # print(target_value, "node is removed.")
                return
            ptr_to_prev = node
        
        # print("There is no such a value.")
        

    def find(self, target_value):
        if self.head is None:
            print("Is empty")

        for node in self:
            if node.key == target_value:
                # print(target_value, "is found.")
                return node.value
        
        # print("There is no such a value.")
