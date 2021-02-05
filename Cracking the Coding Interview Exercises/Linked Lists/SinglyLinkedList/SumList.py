'''

2.5 Sum Lists:

You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.

EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
'''


from LinkedList import LinkedList

def convert(head):
    """This function is use to create string from linked list elements"""
    temp = head
    num = ""
    while temp:
        num = f"{num}{temp.data}"
        temp = temp.next
    return int(num)

def Sumlist(h1,h2):
    """This function create add two linked lists and create new linked list of an answer and return head of that LinkedList"""
    s1 = convert(h1)
    s2 = convert(h2)
    res = str(s1+s2)
    global ll
    ll = LinkedList()
    for i in str(res):
        ll.add(int(i))
    return ll.head

obj1 = LinkedList()
obj2 = LinkedList()


obj1.add(6)
obj1.add(1)
obj1.add(7)

obj2.add(2)
obj2.add(9)
obj2.add(5)

h = Sumlist(obj1.head,obj2.head)
temp = h
while temp:
    print(f"{temp.data}  -> ", end="")
    temp = temp.next