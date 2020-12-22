''' Check the iTh bit is 1 or 0 from right '''

def iThBitFromRight(n, k):
    for i in range(k-1):
        n = n >> 1
    return n & 1
print(iThBitFromRight(11,2))