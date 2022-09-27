print("welcome to the rollercoaster")
height = int(input("what is your height in cm?:"))
if height > 120:
    print("you can ride the rollercoaster")
    age = int(input("what is your age? "))
    if age <= 18:
        print("please pay 7$")
    else:
        print("please pay 12$")
else:
    print("you have to grow taller before you ride!")