class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class DLinkedList:
    def __init__(self):
        self.head = None
        self.count = 1
    
    def append(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            return self
        
        itr = self.head
        while itr:
            if itr.next is None:
                itr.next  = Node(data, None, itr)
                self.count+=1
                return self
                break
            itr = itr.next
    
    @property
    def print(self):
        if self.head is None:
            print("Empty list")
            return self
        itr = self.head
        dllist = ""
        suffix = " <-- --> "
        prefix = ""
        while itr:
            if itr.next is None:
                suffix = " <-- --> None"
            elif itr == self.head:
                prefix = "None <-- --> "
            dllist += prefix + str(itr.data) + suffix
            prefix = ""
            itr = itr.next
        print(dllist)
        print(f"Number of nodes : {self.count}")
        return self
    
    def insert(self, loc, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            self.count += 1
            return self
        if loc == 0:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
            self.count += 1
            return self

dllist = DLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.insert(0, 0)
dllist.print