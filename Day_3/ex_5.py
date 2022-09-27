# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
comb_name = name1 + name2
comb_name.lower()

t = comb_name.count('t')
r = comb_name.count('r')
u = comb_name.count('u')
e = comb_name.count('e')

true = t + r + u + e

l = comb_name.count('l')
o = comb_name.count('o')
v = comb_name.count('v')
e = comb_name.count('e')

love = l + o + v + e

love_score = str(true) + str(love)
score = int(love_score)
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40) and (score < 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")



