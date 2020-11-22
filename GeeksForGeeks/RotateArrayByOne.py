'''Given an array, cyclically rotate an array by one.

Input:
The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow.
Each test case contains an integer n denoting the size of the array.
Then following line contains 'n' integers forming the array.

Link for this problem is Given below:

https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one/0#

'''
def rotateAnArray(n,arr):
    first = arr[len(arr)-1]
    for i in range(len(arr)-1,-1,-1):
        arr[i]=arr[i-1];
    arr[0]=first;
    for i in arr:
        print(i,end=" ")

t = int(input())
while t > 0 :
    t-=1;
    n=int(input())
    arr=[];
    for i in range(n):
        temp=input()
        arr.append(temp)
    rotateAnArray(n,arr)


    
    