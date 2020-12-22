''' Check the iTh bit is 1 or 0 from right '''

def iThBitFromRight(n, k):
    return (n & (1 << k-1))!=0

print(iThBitFromRight(7,3))