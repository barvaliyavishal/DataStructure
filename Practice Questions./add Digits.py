def add(n):
    if n == 0:
        return 0
    return n%10+add(n//10)
print(add(1234))