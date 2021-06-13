# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

print(f'List of Student Heights : {student_heights}')


#Height
total_height = 0
for height in student_heights:
    total_height += height
print(f'Total of Heights : {total_height}')

#No. of Student
number_student = len(student_heights)
print(f'Number of Student : {number_student}')

#Average 
Average = total_height/number_student
print(f'Average : {Average}')