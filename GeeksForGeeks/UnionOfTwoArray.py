'''Given two arrays A and B of size N and M respectively.
 The task is to find union between these two arrays.

 Link for this problem is given Below;

 https://practice.geeksforgeeks.org/problems/union-of-two-arrays/0
 
 '''
def Union(arr1,arr2):
    union = {};
    for i in arr1:
        if i not in union.keys():
            union[i] = i;
    for i in arr2:
        if i not in union.keys():
            union[i] = i;
    for i in union:
        print(i,end=" ")

Union([1,2,3,4,5],[8,4,1,6,9,2,5])

