'''
This is problem of EASY Level from GeeksforGeeks
called Count pairs with given sum
and link for this problem is  given Below:
https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1

Given an array of N integers, and an integer K,
find the number of pairs of elements in the array whose sum is equal to K.

Example 1:
Input:
N = 4, K = 6
arr[] = {1, 5, 7, 1}
Output: 2
Explanation:
arr[0] + arr[1] = 1 + 5 = 6
and arr[1] + arr[3] = 5 + 1 = 6.

'''
def getPairsCount(arr, n, k):
    res=0;
    temp={};
    for i in arr:
        j=k-i;
        if i in temp.keys():
            res+=temp[i];
            if j in temp.keys():
                temp[j]+=1;
            else:
                temp[j]=1;
        else:
            if j in temp.keys():
                temp[j]+=1;
            else:
                temp[j]=1;

    return res;