def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
n = int(input("enter a value: "))
res = fact(n)
print("factorial is",res)