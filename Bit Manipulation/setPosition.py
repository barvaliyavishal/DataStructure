''' set 1 at iTh bit from right '''

def setBit(n, k):
    return (n | (1 << k-1))

print(setBit(4,1))