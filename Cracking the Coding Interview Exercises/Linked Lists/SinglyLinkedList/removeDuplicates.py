from LinkedList import LinkedList


class RemoveDuplicates:
    # Remove duplicates Using O(n^2)
    def removeDuplicates(self, head):
        if head.data is None:
            return

        temp = head
        while temp.next:
            start = temp
            while start.next:
                if start.next.data == temp.data:
                    start.next = start.next.next
                else:
                    start = start.next
            temp = temp.next


obj = LinkedList()

obj.add(1)
obj.add(2)
obj.add(3)
obj.add(3)
obj.add(4)
obj.add(5)
obj.add(7)
obj.add(9)
obj.add(2)
obj.add(2)


print("Before Removing Duplicates")
obj.show()
obj1 = RemoveDuplicates()
obj1.removeDuplicates(obj.head)
print()
print("After Removing Duplicates")
obj.show()
