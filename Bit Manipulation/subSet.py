'''

Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

'''
def subSet(arr,n):
    for i in range(1 << n):
        for j in range(0, i):
            if i & (1 << j):
                print(arr[j], end=" ")
        print()

subSet([1,2,3],3)