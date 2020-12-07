class Node:
    def __init__(self, value=None):
        self.next = None
        self.data = value

    # To Know the length of linked list;
    def length(self, h):
        total = 0
        temp = h
        while temp:
            temp = temp.next
            total += 1
        return total

    # Insert element at last
    def insertAtLast(self, val, h):
        new = Node(val)
        if h.data == None:
            h.data = val
        else:
            temp = h
            while temp.next:
                temp = temp.next
            temp.next = new

    # remove specific element
    def remove(self, val, h):
        if h.data == None:
            return h
        if h.data == val and h.next == None:
            h.data = None
            return h
        if h.data == val and h.next:
            return h.next
        temp = h
        while temp.next.data != val:
            temp = temp.next
        temp.next = temp.next.next
        return h

    # Print Element
    def show(self, h):
        temp = h
        while temp:
            print(temp.data)
            temp = temp.next

    # Insert element at beginning of the list
    def insertAtBeginning(self, val, h):
        new = Node(val)
        new.next = h
        return new

    # print element in reverse manner
    def printReverse(self, h):
        if h.data == None:
            return
        self.printReverse(h.next)
        print(h.data)


head = Node()
obj = Node()
obj.insertAtLast(5, head)
obj.insertAtLast(6, head)
obj.insertAtLast(7, head)
obj.insertAtLast(8, head)
obj.insertAtLast(8, head)
obj.insertAtLast(9, head)

head = obj.remove(8, head)
obj.show(head)
head = obj.insertAtBeginning(4, head)
