'''Given two sorted arrays arr1[] of size N and arr2[] of size M.
 Each array is sorted in non-decreasing order.
 Merge the two arrays into one sorted array in
 non-decreasing order without using any extra space.

 Link for this problem in geeksforgeeks is given Below:

 https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1#
'''

def merge(arr1, arr2, n, m):
    i = n - 1
    j = m - 1
    temp = 0

    while j >= 0:
        if arr2[j] > arr1[i]:
            j -= 1
        else:
            temp = arr2[j]
            arr2[j] = arr1[i]
            j -= 1
            index = n - 1
            while (index >= 0):
                if index == 0:
                    arr1[index] = temp
                    break

                if arr1[index - 1] < temp:
                    arr1[index] = temp
                    break
                else:
                    arr1[index] = arr1[index - 1]
                    index -= 1

a1 = [1,3,5,7,9,9,11,11,13,15,15,15]
a2 = [0,2,6,8,9,10,11,15,15,16,18,18]
merge(a1,a2,len(a1),len(a2))
for i in a1:
    print(i,end=" ")
for i in a2:
    print(i,end=" ")






