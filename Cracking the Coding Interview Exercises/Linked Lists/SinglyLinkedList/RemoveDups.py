from LinkedList import LinkedList


class RemoveDuplicates:
    # Remove duplicates Using O(n)
    def removeDuplicates(self, h):
        if h is None:
            return

        current = h
        seen = set([current.data])

        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next


obj = LinkedList()

obj.add(1)
obj.add(2)
obj.add(3)
obj.add(3)
obj.add(4)
obj.add(5)
obj.add(7)
obj.add(9)
obj.add(9)
obj.add(2)


print("Before Removing Duplicates")
obj.show()
obj1 = RemoveDuplicates()
obj1.removeDuplicates(obj.head)
print()
print("After Removing Duplicates")
obj.show()
