#Write your code below this row 👇

for num in range(1,100):
    if num % 3 == 0:
        print(f"{num} : Fizz")
    elif  num % 5 == 0:
        print(f"{num} : Buzz")
    elif (num % 3) and (num%5) ==0:
        print(f"{num} : FizzBuzz")
    else:
        print(num)            

