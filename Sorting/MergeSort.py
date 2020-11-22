def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2;
        l = arr[:mid];
        r = arr[mid:];
        mergeSort(l);
        mergeSort(r);
        i=j=k=0;
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k]=l[i];
                i+=1;
            else:
                arr[k]=r[j];
                j+=1;
            k+=1;
        while i < len(l):
            arr[k]=l[i];
            i+=1;
            k+=1;
        while j < len(r):
            arr[k]=r[j];
            j+=1;
            k+=1;
    return arr;

arr1 = mergeSort([10,5,9,7,5,99,85,45])
for i in arr1:
    print(i,end=" ")

