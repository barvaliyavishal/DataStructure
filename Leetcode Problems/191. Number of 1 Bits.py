'''
191. number of 1 Bits

Write a function that takes an unsigned integer and
returns the number of '1' bits it has
'''
def numOfOnes(n: int) -> int:
    if n == 0:
        return 0
    res = 1
    temp = n & n-1
    while temp > 0:
        res += 1
        temp = temp & temp-1
    return res
print(numOfOnes(7))