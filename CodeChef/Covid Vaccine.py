def covid(d1, v1, d2, v2, p):
    if d1==d2==1:
        t = 0;
        d = 0;
        while t < p:
            d+=1;
            t+=(v1+v2);
        return d;


    days = 0
    total = 0
    t1 = 0
    t2 = 0

    if d1 > 2:
        t1 = (d1-1)*v1
    if d2 > 2:
        t2 = (d2-1)*v2

    total = t1 + t2

    if total >= p:
        return 0
    temp = max(d1, d2)
    if temp > 2:
        days = temp - 2
    while total < p:
        total += (v1+v2)
        days += 1
    return days



n = input();
fields = n.split(" ")
d1 = int(fields[0])
v1 = int(fields[1])
d2 = int(fields[2])
v2 = int(fields[3])
p = int(fields[4])
a = covid(d1, v1, d2, v2, p)
print(a)
