from LinkedList import LinkedList, Node


def reverse(head):
    temp = None
    while head:
        newnode = Node(head.data)
        if temp:
            newnode.next = temp
            temp = newnode
        else:
            temp = newnode
        head = head.next
    return temp


def is_palindrome(head):
    rev = reverse(head)
    while head:
        if rev.data != head.data:
            return False
        rev = rev.next
        head = head.next
    return True


obj = LinkedList()
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(3)
obj.add(2)
# obj.add(2)
obj.add(1)
# obj.add(1)

print(is_palindrome(obj.head))
