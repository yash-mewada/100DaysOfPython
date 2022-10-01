def pattern(n):
    for i in range(n+1):
        for j in range(i):
            print("*",end=" ")
        print()
rows = int(input("enter number of rows:"))
pattern(rows)