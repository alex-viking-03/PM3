from enum import unique

print("Task 1")
print()

numbers = [2, 4, 7, 8, 10]
print(f"Sum of all values from list is {sum(numbers)}")

print()
print("Task 2")
print()

numbers = [2, 4, 7, 8, 10]
print(f"The greatest number in the list {max(numbers)}")

print()
print("Task 3")
print()

numbers = [2, 4, 7, 8, 10]
print(f"The smallest number in the list {min(numbers)}")

print()
print("Task 4")
print()

numbers = [2, 4, 7, 8, 10]
print(f"Amount of elements in list is {len(numbers)}")

print()
print("Task 5")
print()

numbers = [2, 4, 7, 8, 10]
for i in numbers:
    if i % 2 == 0:
        print(i)

print()
print("Task 6")
print()

numbers = [12, 4, 74, 8, 10]
for i in numbers:
    if i > 10:
        print(i)

print()
print("Task 7")
print()

numbers = [12, 4, 74, 8, 10]
for i in numbers:
    i*=2
    print(i)

print()
print("Task 8")
print()

numbers = [12, 4, 74, 8, 10]
print(f"The arithmetic mean of the list is {sum(numbers)/len(numbers)}")

print()
print("Task 9")
print()

numbers = [12, -4, 74, 8, -10]
for i in numbers:
    if i >= 0:
        print(i)

print()
print("Task 10")
print()

numbers = [12, -4, 74, 8, -10]
for i in numbers:
    if i < 0:
        print(i)

print()
print("Task 11")
print()

numbers = [12, -4, 74, 8, -10]
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0
print(numbers)

print()
print("Task 12")
print()

words = ["extreme", "saying", "pomelo", "new", "bear"]
for i in words:
    if len(i) > 5:
        print(i)

print()
print("Task 13")
print()

numbers = [12, 5, -4, 5, 74, 8, -10, 5]
counter = 0
for i in numbers:
    if i == 5:
        counter += 1
print(f"{counter} times 5")

print()
print("Task 14")
print()

numbers = [12, 5, -4, 5, 74, 8, -10, 5]
print(f"Reversed list: {reversed(numbers)}")

print()
print("Task 15")
print()

numbers = [12, 5, -4, 5, 74, 8, -10, 5]
numbersSqrd = []
for i in numbers:
    numbersSqrd.append(i ** 2)
print(numbersSqrd)

print()
print("Task 16")
print()

students = {"001": {"name": "Aron", "age":"16", "grade": "80"}, "002": {"name": "Alex", "age": "17", "grade": "75"},
            "003": {"name": "Alisher", "age": "17","grade": "83"}, "004": {"name": "Kolya", "age": "16", "grade": "73"}}
for key, value in students.items():
    print(f"{key}: {value}\n")

print()
print("Task 17")
print()

students = {"001": {"name": "Aron", "age":"16", "grade": "80"}, "002": {"name": "Alex", "age": "17", "grade": "75"},
            "003": {"name": "Alisher", "age": "17","grade": "83"}, "004": {"name": "Kolya", "age": "16", "grade": "73"}}

for key, value in students.items():
    students[key]["city"] = "Aktobe"
    print(f"{key}: {value}")

print()
print("Task 18")
print()

students = {"001": {"name": "Aron", "age":"16", "grade": "80"}, "002": {"name": "Alex", "age": "17", "grade": "75"},
            "003": {"name": "Alisher", "age": "17","grade": "83"}, "004": {"name": "Kolya", "age": "16", "grade": "73"}}
for key, value in students.items():
    students[key].pop("age")
    print(f"{key}: {value}")

print()
print("Task 19")
print()

students = {"001": {"name": "Aron", "age":"16"}, "002": {"name": "Alex", "age": "17", "grade": "75"},
            "003": {"name": "Alisher", "age": "17","grade": "83"}, "004": {"name": "Kolya", "age": "16"}}
for key, value in students.items():
    if "grade" in students[key]:
        print(f"{key}: {value}")

print()
print("Task 20")
print()

students = {"001": {"name": "Aron", "age":"16", "grade": "80"}, "002": {"name": "Alex", "age": "17", "grade": "75"},
            "003": {"name": "Alisher", "age": "17","grade": "83"}, "004": {"name": "Kolya", "age": "16", "grade": "73"}}
for value in students.values():
    print(value)

print()
print("Task 21")
print()

students = {"001": {"name": "Aron", "age":"16", "grade": "80"}, "002": {"name": "Alex", "age": "17", "grade": "75"},
            "003": {"name": "Alisher", "age": "17","grade": "83"}, "004": {"name": "Kolya", "age": "16", "grade": "73"}}
for key in students.keys():
    print(key)

print()
print("Task 22")
print()

students = {"001": {"name": "Aron", "age":"16", "grade": "65"}, "002": {"name": "Alex", "age": "17", "grade": "75"},
            "003": {"name": "Alisher", "age": "17","grade": "68"}, "004": {"name": "Kolya", "age": "16", "grade": "73"}}
print(f"Amount of elements in dictionary: {len(students)}")

print()
print("Task 23")
print()

students = {"001": {"name": "Aron", "age":"16", "grade": "65"}, "002": {"name": "Alex", "age": "17", "grade": "75"},
            "003": {"name": "Alisher", "age": "17","grade": "68"}, "004": {"name": "Kolya", "age": "16", "grade": "73"}}
for key, value in students.items():
    if 70 > int(value["grade"]) > 0:
        print(f"{key}: didn't pass")
    elif 100 >= int(value["grade"]) >= 70:
        print(f"{key}: passed")
    else:
        print("There is no such grade")

print()
print("Task 24")
print()

students = {"001": {"name": "Aron", "age":"16", "grade": "65"}, "002": {"name": "Alex", "age": "17", "grade": "75"},
            "003": {"name": "Alisher", "age": "17","grade": "68"}, "004": {"name": "Kolya", "age": "16", "grade": "73"}}
studentsGrades = {}
for key, value in students.items():
    studentsGrades[key] = value["grade"]

for key, value in studentsGrades.items():
    print(f"{key}: {value}")

print()
print("Task 25")
print()

students = {"001": {"name": "Aron", "age":"16", "grade": "65"}, "002": {"name": "Alex", "age": "17", "grade": "75"},
            "003": {"name": "Alisher", "age": "17","grade": "68"}, "004": {"name": "Kolya", "age": "16", "grade": "73"}}
theBestStudent = None
theHighestGrade = 0
for value in students.values():
    if int(value["grade"]) > theHighestGrade:
        theHighestGrade = int(value["grade"])
        theBestStudent = value["name"]
print(f"Best student: {theBestStudent}\nScores: {theHighestGrade}")

print()
print("Task 26")
print()

numbers = [12, 5, -4, 5, 74, 8, -10, 5]
numbersSqrd = {}
for i in numbers:
    numbersSqrd[i] = i**2
print(numbersSqrd)

print()
print("Task 27")
print()

names = ["Harry", "Dmitriy", "Robin", "Vasilisa"]
namesLen = {}
for i in names:
    namesLen[i] = len(i)
print(namesLen)

print()
print("Task 28")
print()

num = int(input("Enter a number: "))
numbers = []
while num != 0:
    numbers.append(num)
    num = int(input("Enter a number: "))
print(numbers)

print()
print("Task 29")
print()

numbers = [12, 5, -4, 5, 74, 8, -10, 5]
uniqueNumbers = []
for i in numbers:
    if i not in uniqueNumbers:
        uniqueNumbers.append(i)
print(uniqueNumbers)

print()
print("Task 30")
print()

students = {"Aron": "80", "Alex": "75",
            "Alisher": "83", "Kolya": "73"}
arithmeticMean = 0
for key, value in students.items():
    arithmeticMean += int(value)
print(f"The arithmetic mean of scores of the group: {arithmeticMean/len(students)}")