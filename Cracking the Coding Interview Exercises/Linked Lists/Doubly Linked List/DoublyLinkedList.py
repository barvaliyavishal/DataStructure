class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.pre = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        new:Node = Node(val)
        if self.head == None:
