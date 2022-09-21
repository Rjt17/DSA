class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, data):

        #when the list is empty i.e. there is no head node
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            self.count += 1
            return self

        #when the list is not empty
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = node(data, itr, None)
        self.count += 1
        return self

    @property
    def print(self):

        #if the list is empty
        if self.head is None:
            print("Empty list")
            return self
        
        #if list has nodes
        