''' set 0 in given position from right (1 indexed from right)
in binary form of given integer 'n'  '''

def clearBit(n, k):
    return (n & ~(1 << k-1))

print(clearBit(7,2))