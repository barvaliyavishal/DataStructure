from LinkedList import LinkedList

class KthToLastElement:
    def kthlast(self, k, h):
        if h is None:
            return 0
        index = self.kthlast(k, h.next)+1
        if index == k:
            print(h.data)
        return index


o = LinkedList()

o.add(1)
o.add(2)
o.add(3)
o.add(4)
o.add(5)
o.add(6)
o.add(7)
res= KthToLastElement().kthlast(6, o.head)
