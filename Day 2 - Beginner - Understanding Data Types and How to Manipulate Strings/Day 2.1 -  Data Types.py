#Type Error, Type Checking and Type Conversion:

num_char = len(input("What is your name? "))

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")
#=============================================================================

#     [Interactive Coding Exercise] Data Types

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

first_digit = two_digit_number[0]
print("First No.: " +first_digit)

second_digit = two_digit_number[1]
print("Second No.: " +second_digit)

result = int(first_digit) + int(second_digit)
print(result)