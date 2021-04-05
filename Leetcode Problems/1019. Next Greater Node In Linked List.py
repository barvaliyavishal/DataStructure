# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        mylist = []
        stack = []
        while head:
            mylist.append(head.val)
            head = head.next

        for i in range(len(mylist) - 1, -1, -1):
            ele = 0
            while len(stack) > 0:
                if stack[-1] > mylist[i]:
                    ele = stack[-1]
                    break
                else:
                    stack.pop()

            res.append(ele)
            stack.append(mylist[i])
        res.reverse()
        return res