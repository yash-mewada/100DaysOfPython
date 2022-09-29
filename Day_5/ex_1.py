# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_students = 0
for no_of_student in student_heights:
    total_students += 1
sum_of_heights = 0
for total_height in student_heights:
    sum_of_heights += total_height

avg = round(sum_of_heights / total_students)
print(avg)


