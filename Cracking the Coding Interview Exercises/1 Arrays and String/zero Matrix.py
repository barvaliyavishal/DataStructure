'''1.8 Zero Matrix: Write an algorithm such that if an element in an
MxN matrix is 0, its entire row and
column are set to 0.'''

def zeromateix(arr):
    r = []  # for rows
    c = []  # for columns

    ''' in below for loop if on specific location in matrix value is 0 .
    then, pick that row and column for reference... '''
    for i in range(len(arr[0])):
        for j in range(len(arr[1])):
            if arr[i][j] == 0:
                r.append(i)
                c.append(j)

    '''In this loop if row or column is present in given row and column array.
     then, we will put zero in that specific row or column'''
    for i in range(len(arr[0])):
        for j in range(len(arr[1])):
            if i in r or j in c:
                arr[i][j] = 0
    return arr


q = zeromateix([
    [1, 2, 3],
    [4, 4, 6],
    [7, 8, 0]]
)
# printing result
for i in range(len(q[0])):
    for j in range(len(q[1])):
        print(q[i][j], end=" ")
    print()
