class Solution:
    def minInsertions(self, s: str) -> int:
        l=0
        r=0
        s=s.replace("))","}")
        for i in s:
            if i=="(":
                l+=1
            elif i==")":
                if l>0:
                    r+=1
                    l-=1
                else:
                    r+=2
            else:
                if l>0:
                    l-=1
                else:
                    r+=1
        return r+(l*2)  