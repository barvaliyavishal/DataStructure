'''
2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input:
Output:
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

'''

from LinkedList import LinkedList


def partition(head : LinkedList,mid):
    temp = head
    first = None
    second = None
    f1 = None
    s1 = None
    while temp:
        if temp.data < mid:
            if first == None:
                first = temp
                f1 = temp
            else:
                f1.next = temp
                f1 = f1.next

        else:
            if second == None:
                second = temp
                s1 = second
            else:
                s1.next = temp
                s1 = s1.next

        temp = temp.next

    f1.next = second
    obj.head = first

obj = LinkedList()
obj.add(3)
obj.add(1)
obj.add(2)
obj.add(10)
obj.add(5)
obj.add(5)
obj.add(8)

h = obj.head
partition(h, 5)
obj.show()

