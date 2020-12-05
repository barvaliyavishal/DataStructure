def pairs(a,b):
    if a==1 or b==1:
        return a*b
    if a%2 == 0:
        a1=a/2
        a2=a/2
    else:
        a1 = int(a//2)+1
        a2 = a//2

    if b%2 == 0:
        b1=int(b/2)
        b2=int(b/2)
    else:
        b1 = int((b//2)+1)
        b2 = int(b//2)
    return int((a1*b1)+(a2*b2))

t = int(input())
while t > 0:
    t -= 1;
    n = input()
    fields = n.split(" ")
    a = int(fields[0])
    b = int(fields[1])
    res = pairs(a,b)
    print(res)
