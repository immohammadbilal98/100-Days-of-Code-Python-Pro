# Number Manpulation and F String in Python
#-------------------------------------------

# Number Manpulation---

print(8/3)
# Ans: 2.666666666666665

print(int(8/3))
# Ans: 2

print(round(8/3))
# Ans: 3

print(round(8/3,2))
# Ans: 2.67

print(round(2.666666666666666,2))
# Ans: 2.67

print(type(8//3)) #class-"int"

print(type(8/3)) #class-"float"
#-----------------------------------------------
# F String in Python ---

#1.
score = 0
print("Your score is " +str(score))

#2.
score = 0
height = 1.8
isWinning = True

#f-String
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#=============================================================================

#     [Interactive Coding Exercise] BMI Calculator

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int = int(age)

year_remaining = 90 - age_as_int
days_remaining = year_remaining * 365
weeks_remaining = year_remaining * 52
month_remaining = year_remaining * 12

message  = f"You have {days_remaining} days, {weeks_remaining} weeks, {month_remaining} month left."
print(message)