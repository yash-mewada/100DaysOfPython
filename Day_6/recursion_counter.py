def counter(n):
    if n<=0:
        return n
    else:
        return n+counter(n-1)
res = counter(5)
print(res)