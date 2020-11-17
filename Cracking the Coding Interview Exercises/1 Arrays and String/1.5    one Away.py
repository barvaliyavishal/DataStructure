'''1.s One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false '''


def oneAway(s1,s2):
    temp=0;
    if len(s1)>len(s2):
        for i in s2:
            if i not in s1:
                return False;
        return True;
    elif len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                temp+=1;
        if temp==1:
            return True;
        else:
            return False;
    elif len(s1) < len(s2):
        if len(s2) - len(s1) > 1:
            return False;
        else:
            return True;


print(oneAway("pale","bae"))








