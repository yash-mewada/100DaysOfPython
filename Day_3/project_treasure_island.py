print(''''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to treasure island")
print("Your mission is to find the treasure")

left_or_right = input("you're at a cross road.where do you want to go? type "'"left" or "right"\n')
if left_or_right == "left" or left_or_right == "LEFT":
    swim_or_wait = input("you come to a lake. there is and island in the middle of the lake. type "'"wait" to wait for a boat.type swim to "swim" across.\n')

    if swim_or_wait == "wait" or swim_or_wait == "wait":
        door = input("you arrive at the island unharmed. there is a house with 3 doors. One,red one yellow and one blue. Which colour do you choose?\n")

        if door == "yellow" or door == "YELLOW":
            print("you win!")
        elif door == "red" or door == "RED":
            print("Burned by fire Game Over")
        elif door == "blue" or door == "BLUE":
            print("eaten by beasts Game Over")
        else:
            print("Game Over")

    else:
        print("attacked by trout Game Over")

else:
    print("fall into hole Game Over")