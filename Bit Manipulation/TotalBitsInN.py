''' return number of bits required to print given integer n'''
def totalBit(n):
    res = 0
    num = 1
    while num < n:
        res += 1
        num *= 2
    return res
print(totalBit(105))