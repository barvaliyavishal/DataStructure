arr = []
for i in range(21):
    arr.append(i+1)
print()
print("First Of All Welcome to this amazing Game")
print()
print("Assume or guess any Number from given Table and follow instruction Given Below")
print()
for i in range(3):
    print("|------+------+------|")
    print("|  1   |   2  |  3   |")
    print("|------+------+------|")
    index = 0
    first = []
    second = []
    third = []
    for j in range(7):
        print("|", end="  ")
        print(arr[index], end="")
        first.append((arr[index]))
        if arr[index] < 10:
            print("   |  ", end="")
        else:
            print("  |  ", end="")
        index += 1
        print(arr[index], end="")
        second.append((arr[index]))
        if arr[index] < 10:
            print("   |  ", end="")
        else:
            print("  |  ", end="")
        index += 1
        print(arr[index], end="")
        third.append((arr[index]))
        if arr[index] < 10:
            print("   |  ", end="")
        else:
            print("  |  ", end="")
        index += 1

        print()
    print("|------+------+------|")


    while(True):
        print()

        k = int(input("Enter the column number in which your number is available  :  "))
        if k == 1:
            ind = 0
            for l in second:
                arr[ind] = l
                ind += 1
            for l in first:
                arr[ind] = l
                ind += 1
            for l in third:
                arr[ind] = l
                ind += 1
            break
        elif k == 3:
            ind = 0
            for l in second:
                arr[ind] = l
                ind += 1
            for l in third:
                arr[ind] = l
                ind += 1
            for l in first:
                arr[ind] = l
                ind += 1
            break
        if k == 2:
            ind = 0
            for l in first:
                arr[ind] = l
                ind += 1
            for l in second:
                arr[ind] = l
                ind += 1
            for l in third:
                arr[ind] = l
                ind += 1
            break
        else:
            print("enter Valid input please!!!");
print()
print()
print("***********************************************")
print()
print()
print("Congratulations!!! I Found Your Number Which is  :  ", arr[10])
