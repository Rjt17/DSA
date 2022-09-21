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
        
        itr.next = Node(data, itr, None)
        self.count += 1
        return self

    @property
    def print(self):

        #if the list is empty
        if self.head is None:
            print("Empty list")
            return self
        
        #if list has nodes
        itr = self.head
        dllist = "None <-- "
        suffix = ' <=> '
        while itr:
            if itr.next is None:
                suffix = ' --> None'
            dllist += str(itr.data) + suffix
            itr = itr.next
        print(dllist)
        return self
    
    #just for debugging
    @property
    def print_all(self):
        itr = self.head
        while itr:
            print(str(itr.prev) + ", " + str(itr) + ", " + str(itr.next) + "<=>")
            itr = itr.next
    #############################################################################
        
    def insert(self, loc, data):
        if loc == self.count:
            self.append(data)
            return self
        if loc == 0:
            node = Node(data, None, self.head)
            self.head = node
            self.head.next.prev = self.head
            return self
        
        
dll = DLinkedList()
dll.print
dll.append(1)
dll.append(2)
dll.print
dll.insert(0, 22)
dll.print
