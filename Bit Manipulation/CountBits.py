'''
Given a non negative integer number num.
 For every numbers i in the range 0 ≤ i ≤ num c
 alculate the number of 1's in their binary representation
 and return them as an array.
'''

def countBits(num: int):
    lst = []
    for i in range(num + 1):
        temp = i
        sets = 0
        while temp > 0:
            if temp & 1:
                sets += 1
            temp = temp >> 1
        lst.append(sets)
    return lst

print(countBits(5))