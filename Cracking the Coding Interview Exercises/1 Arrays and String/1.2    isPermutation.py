#1.2 Check Permutation: Given two strings,
# write a method to decide if one is a permutation of the other.


def isPermutation(str1,str2):
    if len(str1) != len(str2):
        return False;
    chars = {};
    for i in str1:
        if i in chars:
            chars[i]+=1;
        else:
            chars[i]=1;
    for i in str2:
        if i in chars and chars[i]!=0:
            chars[i]-=1
        else:
            return False;
    return True;

print(isPermutation("abqwcd","acwdbq"))
