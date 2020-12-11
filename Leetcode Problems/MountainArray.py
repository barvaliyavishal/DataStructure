def mountain(arr):
    if len(arr) < 3:
        return False
    flag = True

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return False
        if flag:
            if arr[i] > arr[i+1]:
                flag = False
        else:
            if arr[i] <= arr[i+1]:
                return False
    return True

print(mountain([3,5,3,2,1,0,-1,-2]))