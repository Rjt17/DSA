"""
linkedList.py

self.data is the data of linked list node.
self.next is the next to the next node of linked list.
self.head is the head node of linked list.
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    @property
    def print(self):
        if self.head is None:
            print("Empty List")
            return
        
        itr = self.head
        llist = ""
        suffix = " --> "
        while itr:
            if itr.next is None:
                suffix = " --> None"
            llist += str(itr.data) + suffix
            itr = itr.next
        print(llist)

    @property
    def count(self):
        if self.head is None:
            return 1
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count+=1
        return count
        
    def append(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = node
    
    def insert(self, index, data):
        if index < 0 or index > self.count:
            raise Exception("Linked List index out of range")
        
        if index == 0:
            node = Node(data, self.head)
            self.head = node
            return
        
        if index == self.count:
            self.append(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1

    def pop(self, index):
        if index < 0 or index > self.count-1:
            raise Exception("Linked List index out of range")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
    
    def remove(self, value):
        itr = self.head
        if self.index(value) == 0:
            self.head = itr.next
            return
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next
    
    def index(self, value):
        count = 0
        itr = self.head
        while itr:
            if itr.data == value:
                return count
                break
            itr = itr.next
            count+=1
    
    def find(self, index, boolean):
        if index < 0 or index > self.count-1:
            raise Exception("Linked List index out of range")
        
        itr = self.head
        count = 0
        while itr:
            if count == index:
                if boolean == 1:
                    return itr.data
                    break
                else:
                    return itr
                    break
            itr = itr.next
            count+=1

    def update(self, index, value):
        if index < 0 or index > self.count-1:
            raise Exception("Linked List index out of range")
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.data = value
            itr = itr.next
            break
    
    def insert_bulk(self, index, values):
        if index < 0 or index > self.count:
            raise Exception("Linked List index out of range")
        
        if index == self.count:
            for value in values:
                self.append(value)
            return
        count = 0
        if index == 0:
            for value in values:
                self.insert(count, value)
                count+=1
            return


        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                for loc, value in enumerate(values):
                    print(loc, value)
                    loc+=index
                    self.insert(loc, value)
                break
            itr = itr.next
            count+=1

        



#Calling
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.print
llist.insert(3, 4)
llist.print
print(llist.count)
llist.pop(3)
llist.print
print(llist.index(2))
obj1 = llist.find(1, 0)
print(obj1)
print(obj1.data)
llist.update(0, 0)
llist.print
llist.remove(2)
llist.remove(0)
llist.remove(3)
llist.print
llist.insert_bulk(1, [10,20,30])
llist.print