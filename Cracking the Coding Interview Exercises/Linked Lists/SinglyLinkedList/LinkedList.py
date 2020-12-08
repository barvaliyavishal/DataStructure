class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    # add element to Linked list
    def add(self, val):
        node: Node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.len = 1
        else:
            self.tail.next = node
            self.tail = self.tail.next
            self.len += 1

    # show all elements of Linked List
    def show(self):
        temp = self.head
        while temp:
            print(temp.data," -> ",end="")
            temp = temp.next

    # Remove specific element from linked list
    def remove(self, val):
        if self.head is None:
            return
        temp = self.head
        while temp.next:
            if temp.next.data == val:
                temp.next = temp.next.next
                self.len -= 1
            temp = temp.next

    # add element at the beginning of the list
    def addAtBeginning(self, val):
        node: Node = Node(val)
        node.next = self.head
        self.head = node
        self.len += 1

    # get the length of linked list
    def length(self):
        return self.len

