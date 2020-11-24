'''Find minimum number of merge operations to make an array palindrome

Link for this problem is given below:

https://www.geeksforgeeks.org/find-minimum-number-of-merge-operations-to-make-an-array-palindrome/

'''
def mergeOperations(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] != arr[n-(i+1)]:
            return (n-(i*2))-1;
print(mergeOperations([11, 14, 15, 99]))
