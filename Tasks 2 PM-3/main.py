print("Task 1")
print()

num = int(input("Enter a number: "))
if num <= 10:
    print("Small")
else:
    print("Big")

print()
print("Task 2")
print()

for i in range(1, 11):
    print(i)

print()
print("Task 3")
print()

for i in range(2, 21, 2):
    print(i)

print()
print("Task 4")
print()

num = int(input("Enter a number: "))
for i in range(1, num + 1):
    print(i)

print()
print("Task 5")
print()

num = int(input("Enter a number: "))
if num% 2 == 0:
    print("Even")
else:
    print("Odd")

print()
print("Task 6")
print()

result = 0
for i in range(101):
    result += i
print(f"Sum of numbers from 1 to 100 equals {result}")

print()
print("Task 7")
print()

num = int(input("Enter a number: "))
result = 0
for i in range(1, num + 1):
    result += i

print(f"Sum of numbers from 1 to {num} equals {result}")

print()
print("Task 8")
print()

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

print()
print("Task 9")
print()

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
num5 = int(input("Enter the fifth number: "))

print(f"Average value: {(num1 + num2 + num3 + num4 + num5) / 5}")

print()
print("Task 10")
print()

num = int(input("Enter a number: "))
result = 0
while num > 0:
    num //= 10
    result += 1
print("Number of digits is", result)

print()
print("Task 11")
print()

num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} greater than 0")
elif num < 0:
    print(f"{num} less than 0")
else:
    print(f"{num} equal to 0")

print()
print("Task 12")
print()

num = int(input("Enter a number: "))
for i in range(num, 0, -1):
    print(i)

print()
print("Task 13")
print()

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))
num5 = int(input("Enter a number: "))
num6 = int(input("Enter a number: "))
num7 = int(input("Enter a number: "))
num8 = int(input("Enter a number: "))
num9 = int(input("Enter a number: "))
num10 = int(input("Enter a number: "))

listOfNumbers = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
counter = 0

for num in listOfNumbers:
    if num > 0:
        counter += 1

print("Number of positive numbers is", counter)

print()
print("Task 14")
print()

number = int(input("Enter a number: "))
counter = 0

while number > 0:
    addition = number % 10
    number //= 10

    counter += addition
print(f"Sum of numbers equals {counter}")

print()
print("Task 15")
print()

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} divisible by 3 and 5")
else:
    print(f"{num} isn't suitable")

print()
print("Task 16")
print()

num = int(input("Enter a number: "))
counter = 0

while num != 0:
    counter += num
    num = int(input("Enter a number: "))
print(f"Sum of numbers equals {counter}")

print()
print("Task 17")
print()

num = int(input("Enter a number: "))
for i in range(1, num + 1, 2):
    print(i)

print()
print("Task 18")
print()

num = int(input("Enter a number: "))
if num == 0 or num == 1:
    print(f"{num} is not perfect number")

else:
    isPerfect = True
    for i in range(2, num):
        if num % i == 0:
                isPerfect = False
                break

    if isPerfect:
        print(f"{num} is perfect number")
    else:
        print(f"{num} is not perfect number")

print()
print("Task 19")
print()

n = int(input("Enter a number: "))
counter = 1
for i in range(1, n + 1):
    counter *= i
print(f"Factorial of {n} is {counter}")

print()
print("Task 20")
print()

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
num5 = int(input("Enter the fifth number: "))
num6 = int(input("Enter the sixth number: "))
num7 = int(input("Enter the seventh number: "))

listOfNumbers = [num1, num2, num3, num4, num5, num6, num7]

print(f"The maximum value: {max(listOfNumbers)}")
print(f"The minimum value: {min(listOfNumbers)}")