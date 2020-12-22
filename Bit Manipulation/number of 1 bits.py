'''
191. number of 1 Bits

Write a function that takes an unsigned integer and
returns the number of '1' bits it has
'''
def numOfOnes(n: int) -> int:
    res = 0
    while n:
        res += 1
        n = n & n - 1
    return res
print(numOfOnes(7))