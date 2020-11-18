'''1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
Hints: #51, # 100'''



def rotateMatrix(arr):

    arr2=[];
    for i in range(len(arr[0])):
        temp = [];
        for j in range(len(arr[1])-1,-1,-1):
            temp.append(arr[j][i]);
        arr2.append(temp)
    return arr2;

a = rotateMatrix([[1,  2,  3,  4],
                  [5,  6,  7,  8],
                  [9,  10, 11, 12],
                  [13, 14, 15, 16]])

for i in range(len(a[0])):
    for j in range(len(a[1])):
        print(a[i][j],end=" ");
    print()


