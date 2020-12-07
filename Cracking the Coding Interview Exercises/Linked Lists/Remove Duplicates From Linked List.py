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

    # Function to remove duplicates from singly linked lists
    # Using O(n^2) time complexity and O(1) space Complexity
    def removeDups(self, h):
        if h.data == None:
            return h

        temp = h
        while(temp.next):
            start = temp
            while(start.next):
                if start.next.data == temp.data:
                    start.next = start.next.next
                else:
                    start = start.next
            temp = temp.next
        return h


head = Node()
obj = Node()
obj.insertAtLast(5, head)
obj.insertAtLast(6, head)
obj.insertAtLast(7, head)
obj.insertAtLast(8, head)
obj.insertAtLast(8, head)
obj.insertAtLast(9, head)
obj.insertAtLast(6, head)
obj.insertAtLast(5, head)
obj.show(head)
print()
print()
head = obj.removeDups(head)
obj.show(head)
