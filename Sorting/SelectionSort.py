def SelectionSort(arr):

    for j in range(len(arr)-1):
        max = j;
        for i in range(j+1,len(arr)-1,1):
            if arr[max] > arr[i]:
                max = i;
        temp = arr[j];
        arr[j] = arr[max];
        arr[max]=temp;
    return arr;

print(SelectionSort([5,7,1,3,2,4,0,8]))
