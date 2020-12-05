def vaccine2(age,n,d):
    risk=0;
    notrisk=0;
    for i in age:
        if i > 9 and i < 80:
            notrisk+=1;
        else:
            risk+=1;
    total=0;
    while(risk>0):
        total+=1;
        risk-=d;
    while(notrisk>0):
        total+=1;
        notrisk-=d;
    return total;


t= int(input());
while t > 0:
    t-=1;
    s=input().split(" ");
    n=int(s[0])
    d=int(s[1])

    a = input().split(" ")
    age=[];
    for i in a:
        age.append(int(i))
    res = vaccine2(age,n,d)
    print(res);
