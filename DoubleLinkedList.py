class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    #just for debugging #ignore
    @property
    def print_all(self):
        itr = self.head
        while itr:
            print(str(itr.prev) + ", " + str(itr) + ", " + str(itr.next) + "<=>")
            itr = itr.next
    ###################

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
        
    def insert(self, loc, data):
        if self.count == 0:
            self.head = Node(data, None, None)
            return self
        if loc < 0 or loc > self.count:
            raise Exception("List index out of range")
            return self
        if loc == self.count:
            self.append(data)
            self.count += 1
            return self
        if loc == 0:
            node = Node(data, None, self.head)
            self.head = node
            self.head.next.prev = self.head
            self.count += 1
            return self
        
        itr = self.head
        index = 0
        while itr:
            if index == loc-1:
                node = Node(data, itr, itr.next)
                itr.next.prev = node
                itr.next = node
                self.count += 1
                return self
            itr = itr.next
            index+=1
    
    def pop(self, loc):
        if self.count == 1:
            self.head = None
            self.count -= 1
            return self
        if loc < 0 or loc > self.count - 1:
            raise Exception("List index out of range")
            return self
        
        if loc == 0:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
            return self
        
        itr = self.head
        index = 0
        while itr:
            if index == loc-1:
                itr.next = itr.next.next
                itr.next.prev = itr
                self.count -= 1
                return self
    
    def remove(self, data):
        if self.count == 1:
            self.head = None
            self.count -= 1
            return self
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
            return self
        
        itr = self.head
        while itr:
            if itr.next is None:
                if itr.data == data:
                    itr.prev.next = None
                    self.count -= 1
                    return self
                    break
            
            if itr.data == data:
                itr.prev.next = itr.next
                itr.next.prev = itr.prev
                self.count -= 1
                return self
            itr = itr.next
        raise Exception("item not found in list")
    
    def index(self, data):
        if self.head is None:
            raise Exception("Item not found in list")

        if self.count == 1:
            return self.count-1

        itr = self.head
        index = 0
        while itr:
            if itr.data == data:
                return index 
            itr = itr.next
            index += 1
        
        raise Exception("Item not found in list")

    @property
    def length(self):
        return self.count
    
    def find(self, loc):
        if loc < 0 or loc > self.count - 1:
            raise Exception("List index out of range")
        if loc == 0:
            return self.head
        itr = self.head
        index = 0
        while itr:
            if index == loc:
                return itr
            itr = itr.next
            index += 1
        raise Exception("List index out of range")

    def update(self, loc, data):
        if self.count == 0:
            raise Exception("List index out of range")
        if loc == 0:
            self.head.data = data
            return self
        node = self.find(loc)
        node.data = data
        return self

    def insert_bulk(self, loc, data_list):
        if loc < 0 or loc > self.count:
            raise Exception("List index out of range")
        
        if loc == self.count:
            for value in data_list:
                self.append(value)
                self.count += 1
            return self
        
        if loc == 0:
            self.insert(0, data_list[0])
            data_list.pop(0)

            for index, value in enumerate(data_list):
                self.insert(index+1, value)
                self.count += 1
            return self
        
        for index, value in enumerate(data_list):
            self.insert(index+loc, value)
            self.count += 1
        return self
    
    @property
    def empty(self):
        self.head = None
        return self

dll = DLinkedList()
dll.print
dll.append(1)
dll.append(2)
dll.print
dll.insert(1, 22)
dll.print
dll.pop(1)
dll.pop(0)
dll.print
dll.remove(2)
dll.print
dll.append(1)
dll.append(2)
dll.append(3)
dll.print
print(dll.index(1))
print(dll.length)
print(dll.find(2))
dll.update(1, 22)
dll.print
dll.pop(0)
dll.pop(0)
dll.pop(0)
dll.insert_bulk(0, [6,7,8])
dll.print
dll.empty
dll.print