'''An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.
Examples :

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5


Note: Order of elements is not important here.

Link for this Problem is Giveb Below:

https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/

'''




def moveNegatives(arr):
    low=0;
    mid=0;
    hi = len(arr)-1;
    while mid<=hi:
        if arr[mid] >=0:
            temp=arr[mid];
            arr[mid]=arr[hi];
            arr[hi]=temp;
            hi-=1;
            mid+=1;
        else:
            temp=arr[low];
            arr[low]=arr[mid];
            arr[mid]=temp;
            low+=1;
            mid+=1;
    return arr;

res = moveNegatives([10,-7,2,5,-8,-9,-4])
for i in res:
    print(i,end=" ");