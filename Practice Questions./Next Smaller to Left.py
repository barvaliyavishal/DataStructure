'''
Given array nums of integers
for each element find nearest smaller element to left if not found put -1

for example

Input :
    Nums : [2,5,1,4,3,6]
Output:
    [-1,2,-1,1,1,3]

Explanation:
    for first element 2 there is no left element so -1
    for 5 left smaller element is 2
    for 1 there is no smaller element so -1
    for 4 left smaller element is 1
    for 3 nearest smaller element is 1
    fpr 6 nearest smaller element is 3

'''


class Solution:
    def NSL(self, nums):
        stack = []
        res = []
        for i in nums:
            if len(stack) == 0:
                res.append(-1)
                stack.append(i)
            else:
                for j in range(len(stack)-1, -1,-1):
                    if stack[j] < i:
                        res.append(stack[j])
                        stack.append(i)
                        break
                    else:
                        stack.pop()
                        if len(stack) == 0:
                            res.append(-1)
                            stack.append(i)
                            break
        return res

obj = Solution()
res = obj.NSL([2,5,1,4,3,6])
print(res)

