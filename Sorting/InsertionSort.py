def InsertionSort(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            for j in range(i,-1,-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j];
                    arr[j]=arr[j+1]
                    arr[j+1]=temp;
    return arr;

print(InsertionSort([3,6,5,7,8,9,1,2]))