'''
86. Partition List
leetcode Question Link : https://leetcode.com/problems/partition-list/


Defination:

Given the head of a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
        Input: head = [1,4,3,2,5,2], x = 3
        Output: [1,2,2,4,3,5]

Example 2:
        Input: head = [2,1], x = 2
        Output: [1,2]
'''


#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        firstStart = None
        firstEnd = None
        secondStart = None
        secondEnd = None

        temp = head
        while temp:
            newnode = ListNode(temp.val)
            if temp.val < x:
                if firstStart == None:
                    firstStart = newnode
                    firstEnd = newnode
                else:
                    firstEnd.next = newnode
                    firstEnd = firstEnd.next
            else:
                if secondStart == None:
                    secondStart = newnode
                    secondEnd = newnode
                else:
                    secondEnd.next = newnode
                    secondEnd = secondEnd.next
            temp = temp.next
        if firstStart == None:
            return secondStart
        firstEnd.next = secondStart
        return firstStart