def nearestGreaterRight(arr):
    res=[];
    for i in range(len(arr)):
        temp = i+1;
        flag=True;
        while temp < len(arr) :
            if arr[i] < arr[temp]:
                res.append(arr[temp])
                flag=False;
                break;
            temp+=1;
        if flag:
            res.append(-1);
    print(res)

arr = [2,5,9,1,3,8,5];
nearestGreaterRight(arr);