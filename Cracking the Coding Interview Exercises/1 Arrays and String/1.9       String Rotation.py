'''1.9 String Rotation: Assume you have a method i 5Su b 5  tr ing which checks
if one word is a substring of another. Given two strings, 51 and 52,
write code to check if 52 is a rotation of 51 using only one call to i5Sub5tring
(e.g., "waterbottle" is a rotation of"erbottlewat"). '''



def isSubString(s1,s2):
    char = {};
    if len(s1)!=len(s2):
        return False;
    for i in s1:
        if i in char.keys():
            char[i]+=1;
        else:
            char[i]=1;
    for i in s2:
        if i in char.keys() and char[i]>0:
            char[i]-=1;
        else:
            return False;
    return True;

print(isSubString("vishal","visla"))