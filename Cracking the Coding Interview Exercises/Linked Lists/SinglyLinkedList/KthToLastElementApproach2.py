from LinkedList import LinkedList


def kth_to_last(head, k):
    if head.next is None:
        return 1
    index = kth_to_last(head.next, k)+1
    if index == k:
        print(f"your element is {head.data}")
    return index


obj1 = LinkedList()
obj1.add(1)
obj1.add(2)
obj1.add(3)
obj1.add(4)
obj1.add(5)
obj1.add(6)
obj1.add(7)
obj1.add(8)

obj1.show()
kth_to_last(obj1.head, 5)