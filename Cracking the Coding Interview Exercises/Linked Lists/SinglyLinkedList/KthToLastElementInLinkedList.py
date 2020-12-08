from LinkedList import LinkedList

class KthToLastElement:
    def kthlast(self, k,h):
        if k > h.length():
            return -1
        temp = h.head
        for i in range(h.length()-k):
            temp = temp.next
        return temp.data


o = LinkedList()

o.add(1)
o.add(2)
o.add(3)
o.add(4)
o.add(5)
o.add(6)
o.add(7)
res= KthToLastElement().kthlast(7,o)
print(res)