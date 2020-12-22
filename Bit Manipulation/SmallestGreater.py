''' Find the Smallest number greater then 'n' ,
    with exactly 1 bit different in binary form'''

def smallestGreater(n):
    temp = n
    res = 1
    while temp & 1:
        res *= 2
        temp = temp >> 1
    return n+res
print(smallestGreater(5))
