'''
This is a problem called "subarray with 0 sum"
and link for this problem is given below...
https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/

Given an array of positive and negative numbers.
 Find if there is a subarray (of size at-least one) with 0 sum.

Example 1:
Input:
5
4 2 -3 1 6
Output:
Yes

Explanation:
2, -3, 1 is the subarray
with sum 0.

'''

def subArrayExists(arr,n):
    res = {};
    sum=0;
    for i in range(n):
        sum+=arr[i];
        if sum==0 or sum in res.keys():
            return True;
        res[sum] = 1;
    return False;