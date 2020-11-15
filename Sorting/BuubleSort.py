def BubbleSort(arr):
    stop=len(arr)-1
    index = 0;
    temp = 0;
    for j in range(len(arr)-1):
        for i in range(stop):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1];
                arr[i+1]=temp;
        stop-=1;
    return arr;

print(BubbleSort([9,3,2,4,6,1,8,7,10,5]))

