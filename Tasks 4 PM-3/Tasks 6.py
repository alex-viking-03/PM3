# print("Task 1")
# print()
#
# numbers = []
# while len(numbers) < 5:
#     numbers.append(int(input("Enter a number: ")))
# print(numbers)
#
# print()
# print("Task 2")
# print()
#
# numbers = []
# usersInput = int(input("Enter a number: "))
# while usersInput != 0:
#     numbers.append(usersInput)
#     usersInput = int(input("Enter a number: "))
# print(numbers)
#
# print()
# print("Task 3")
# print()
#
# finish = int(input("Enter a number: "))
# for i in range(1, finish + 1):
#     print(i)
#
# print()
# print("Task 4")
# print()
#
# listOfNumbers = []
# for i in range(1, 6):
#     toAdd = int(input("Enter a number: "))
#     listOfNumbers.append(toAdd)
#
# print("Maximum value is", max(listOfNumbers))
#
# print()
# print("Task 5")
# print()
#
# listOfNumbers = []
# for i in range(1, 6):
#     toAdd = int(input("Enter a number: "))
#     listOfNumbers.append(toAdd)
#
# print("Minimum value is", min(listOfNumbers))
#
# print()
# print("Task 6")
# print()
#
# listOfNumbers = []
# usersInput = int(input("Enter a number: "))
#
# while usersInput >= 0:
#     listOfNumbers.append(usersInput)
#     usersInput = int(input("Enter a number: "))
#
# print("Maximum value is", max(listOfNumbers))
#
# print()
# print("Task 7")
# print()
#
# number = int(input("Enter a number: "))
# listOfNumbers = []
# for i in range(1, number + 1):
#     listOfNumbers.append(i)
#
# print(listOfNumbers)
# print("Maximum value is", max(listOfNumbers))
#
# print()
# print("Task 8")
# print()
#
# listOfNumbers = []
# maxValue = None
# minValue = None
#
# for i in range(1, 11):
#     toAdd = int(input("Enter a number: "))
#     listOfNumbers.append(toAdd)
#
# for i in listOfNumbers:
#     if maxValue is None or i > maxValue:
#         maxValue = i
#     elif minValue is None or i < minValue:
#         minValue = i
#
# print("Maximum value is", maxValue)
# print("Minimum value is", minValue)
#
# print()
# print("Task 9")
# print()
#
# listOfNumbers = []
# firstMaxValue = None
# secondMaxValue = None
# num = int(input("Enter a number: "))
#
# while num != 0:
#     listOfNumbers.append(num)
#     num = int(input("Enter a number: "))
#
# firstMaxValue = max(listOfNumbers)
#
# for i in listOfNumbers:
#     if secondMaxValue is None or firstMaxValue > i > secondMaxValue:
#         secondMaxValue = i
#
# print("First maximum value:", firstMaxValue)
# print("Second maximum value:", secondMaxValue)
#
# print()
# print("Task 10")
# print()
#
# listOfNumbers = input("Enter list of numbers(by spaces): ").split()
# listOfNumbers = list(map(int, listOfNumbers))
# print(f"The difference between max value and min value: {max(listOfNumbers) - min(listOfNumbers)}")
#
# print()
# print("Task 11")
# print()
#
# listOfNumbers = []
# num = int(input("Enter a number: "))
#
# while num != 0:
#     listOfNumbers.append(num)
#     num = int(input("Enter a number: "))
# print(f"Amount of numbers in list: {len(listOfNumbers)}\nMax value: {max(listOfNumbers)}")
#
# print()
# print("Task 12")
# print()
#
# listOfNumbers = []
# length = int(input("Enter the length of the list: "))
# for i in range(length + 1):
#     listOfNumbers.append(i)
# print(f"Min value: {min(listOfNumbers)}\nMax value: {max(listOfNumbers)}\nAverage value: {sum(listOfNumbers)/len(listOfNumbers)}")
#
# print()
# print("Task 13")
# print()
#
# listOfNumbers = []
# num = int(input("Enter the number: "))
#
# while num <= 100:
#     listOfNumbers.append(num)
#     num = int(input("Enter the number: "))
#
# print(listOfNumbers)
#
# print()
# print("Task 14")
# print()
#
# listOfNumbers = []
# for i in range(10):
#     num = int(input("Enter the number: "))
#     listOfNumbers.append(num)
#
# for i in listOfNumbers:
#     if i > sum(listOfNumbers)/len(listOfNumbers):
#         print(i)
#
# print()
# print("Task 15")
# print()
#
# listOfNumbers = []
# num = int(input("Enter the number: "))
# botToTop = None
# topToBot = None
#
# while num != 0:
#     listOfNumbers.append(num)
#     num = int(input("Enter the number: "))
#
# for i in range(len(listOfNumbers)-1):
#     if listOfNumbers[i] >= listOfNumbers[i+1]:
#         botToTop = False
#     if listOfNumbers[i] <= listOfNumbers[i + 1]:
#         topToBot = False
#
# if botToTop:
#     print("From min to max")
# elif topToBot:
#     print("From max to min")
# else:
#     print("Chaos")
#
# print()
# print("Task 16")
# print()
#
# listOfNumbers = []
# num = int(input("Enter the number: "))
# counter = 0
#
# while num != 0:
#     listOfNumbers.append(num)
#     num = int(input("Enter the number: "))
#
# for i in listOfNumbers:
#     if i == max(listOfNumbers):
#         counter += 1
# print(f"Max value repeated ({max(listOfNumbers)}) for {counter} times")
#
# print()
# print("Task 17")
# print()
#
# listOfNumbers = []
#
# num = int(input("Enter the number: "))
# counter = 0
#
# while num != 0:
#     listOfNumbers.append(num)
#     num = int(input("Enter the number: "))
#
# minValue = max(listOfNumbers)
#
# for i in listOfNumbers:
#     if i > 0:
#         if i < minValue:
#             minValue = i
#
# print("Min positive value:", minValue)
#
# print()
# print("Task 18")
# print()
#
# length = int(input("Enter the length: "))
# listOfNumbers = []
#
# for i in range(length):
#     num = int(input("Enter the number: "))
#     listOfNumbers.append(num)
#
# if listOfNumbers.count(max(listOfNumbers)) >= 2:
#     print("Max values are repeated")
# else:
#     print("Max values are not repeated")

print()
print("Task 19")
print()

listOfNumbers = []

num = int(input("Enter the number: "))
counter = 1
maxCounter = 1

while num != 0:
    listOfNumbers.append(num)
    num = int(input("Enter the number: "))

for i in range(len(listOfNumbers)-1):
    if listOfNumbers[i+1] - listOfNumbers[i] == 1:
        counter += 1
        maxCounter = max(maxCounter, counter)
    else:
        counter = 1


print(maxCounter)