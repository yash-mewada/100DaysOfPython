def square(side):
    area = side ** 2
    peri = 4 * side
    print("area of square is ",area)
    print("perimeter of square is",peri)
side = int(input("enter value of side:"))
square(side)