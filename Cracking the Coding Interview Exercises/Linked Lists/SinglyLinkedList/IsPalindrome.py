from LinkedList import LinkedList


def is_palindrome(head):
    t = head
    flag = True

    def sub(temp):
        if temp is None:
            return
        sub(temp.next)
        nonlocal flag
        nonlocal head
        if flag and temp.data != head.data:
            flag = False
        head = head.next
    sub(t)
    if flag:
        return "Palindrome"
    else:
        return "Not Palindrome"


obj1 = LinkedList()

obj1.add("e")
obj1.add("a")
obj1.add("b")
obj1.add("c")
obj1.add("b")
obj1.add("a")
obj1.add("e")


res = is_palindrome(obj1.head)
print(res)
