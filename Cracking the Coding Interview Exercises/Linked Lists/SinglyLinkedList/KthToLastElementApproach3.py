from LinkedList import LinkedList


def kth_to_last_element(head, k):
    n = 0
    temp = head
    while head.next:
        n += 1
        if n >= k:
            temp = temp.next
        head = head.next
    return temp.data


obj1 = LinkedList()
obj1.add(1)
obj1.add(2)
obj1.add(3)
obj1.add(4)
obj1.add(5)
obj1.add(6)
obj1.add(7)
obj1.add(8)
obj1.add(9)

res = kth_to_last_element(obj1.head, 5)
print(res)
