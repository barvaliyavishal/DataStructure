def powerOfN(n,p):
    if p == 1:
        return n
    return n * (powerOfN(n,p-1))

a = powerOfN(10,3)
print(a)