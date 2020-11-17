#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def isUnique(name):
    for i in range(len(name)):
        for j in range(i+1,len(name),1):
            if name[i]==name[j]:
                return False;
    return True;
print(isUnique("qnsmeqw"))
