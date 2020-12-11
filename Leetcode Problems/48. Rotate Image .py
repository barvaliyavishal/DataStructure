def rotate(matrix):
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = [0] * 4
            row, col = i, j
            for k in range(4):
                tmp[k] = matrix[row][col]
                row, col = col, n - 1 - row
            for k in range(4):
                matrix[row][col] = tmp[(k - 1) % 4]
                row, col = col, n - 1 - row

arr = [[1,2,3],[4,5,6],[7,8,9]]
rotate(arr)
for i in arr:
    for j in i:
        print(j,end=" ")
    print()