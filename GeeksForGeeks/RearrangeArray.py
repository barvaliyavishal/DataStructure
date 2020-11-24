'''Given an array of positive and negative numbers,
 arrange them in an alternate fashion such that every positive number is
 followed by negative and vice-versa maintaining the order of appearance.
Number of positive and negative numbers need not be equal.
If there are more positive numbers they appear at the end of the array.
If there are more negative numbers,
 they too appear in the end of the array.

Examples :

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}

Link for given problem is :
https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/
'''

def rearrangearray(arr):
    flag = False

    for i in range(len(arr)):
        found = False
        j = i + 1
        if flag == True:
            flag = False
            if arr[i] > 0:
                continue
            while j < len(arr)-1:
                if arr[j] > 0:
                    found = True
                    break
                j += 1
            if not found:
                return arr
            temp = arr[j]
            while j > i:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = temp
        else:
            flag = True
            if arr[i] < 0:
                continue
            while j < len(arr):
                if arr[j] < 0:
                    found = True
                    break
                j += 1
            if not found:
                return arr
            temp = arr[j]
            while j > i:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = temp
    return arr

ar = rearrangearray([-1,-2,-3,-4,5,6,7,8,9,10,11,12])
for i in ar:
    print(i,end=" ")

