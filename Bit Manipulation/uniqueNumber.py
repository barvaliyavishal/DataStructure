'''
unique number in array
'''

def uniqueNumber(arr):
    res = 0
    for i in arr:
        res = res ^ i
    return res
print(uniqueNumber([2,3,6,4,2,3,6,6,3,2]))