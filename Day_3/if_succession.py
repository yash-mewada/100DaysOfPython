print("welcome to the rollercoaster")
height = int(input("what is your height in cm?:"))
bill = 0
if height > 120:
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print("child tickets are 5$")
    elif age <= 18:
        bill = 7
        print("youth tickets are 7$")
    else:
        bill = 12
        print("adult tickets are 12$")
    wants_photo = input("do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print("you can ride the rollercoaster")
    print(f"your final bill is {bill}")
else:
    print("you have to grow taller before you ride!")