'''Given an array of n positive integers and a number k.
Find the minimum number of swaps required to bring all
the numbers less than or equal to k together.

link for this problem in GeeksforGeeks is given below:

https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together/0
'''
def ok(arr,k):
    res = 0;
    counting = False;

    for i in arr:
        if counting:
            if i <= k:
                res += 1;
        elif i > k:
            counting = True;
    return res;

print(ok([2, 7, 9, 5, 8, 7, 4],6))

