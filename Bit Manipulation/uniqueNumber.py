'''
unique number in array
'''

def uniqueNumber(arr):
    res = 0
    for i in arr:
        res = res ^ i
    return res
print(uniqueNumber([2,4,6,3,4,6,2]))