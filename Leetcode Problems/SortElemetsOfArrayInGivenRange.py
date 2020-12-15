def mergeSort(arr, n):
    if len(arr) > 1:
        mid = n//2
        l = arr[:mid]
        r = arr[mid:n]
        mergeSort(l, len(l))
        mergeSort(r, len(r))
        i = j = k = 0;
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

arr1 = [10,5,9,7,5,99,89,65,85,96,85,45]
mergeSort(arr1,5)
for i in arr1:
    print(i,  end=" ")

