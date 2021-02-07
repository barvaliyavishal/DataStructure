from LinkedList import LinkedList

'''
Delete Middle Node: Implement an algorithm to delete a node in the middle 
(i.e., any node but the first and last node,
 not necessarily the exact middle) of a singly linked list, 
 given only access to that node.
EXAMPLE
lnput: the node c is given from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a ->b->d->e->f 
'''


def delete_middle_node(node):
    node.data = node.next.data
    node.next = node.next.next


obj1 = LinkedList()
obj1.add('A')
obj1.add('B')
obj1.add('C')
obj1.add('D')
obj1.add('E')
obj1.add('F')
obj1.add('G')


# delete c
obj1.show()
print("\nDeleting C from LinkedList")
delete_middle_node(obj1.head.next.next)
obj1.show()

# delete head itself
print("\nDeleting Head Itself")
delete_middle_node(obj1.head)
obj1.show()
