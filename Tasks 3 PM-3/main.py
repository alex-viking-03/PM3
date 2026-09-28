print("Task 1")
print()

message = input("Enter your message: ")
if len(message) > 10:
    print("Message is long")
else:
    print("Message is short")

print()
print("Task 2")
print()

message = input("Enter your message: ")
if message.lower().startswith("A"):
    print("Your message starts with A")
else:
    print("Your message does not start with A")

print()
print("Task 3")
print()

message = input("Enter your message: ")
onlyLet = True
for i in message:
    if i.isdigit():
        print("Your message contains one or more numbers")
        onlyLet = False
        break
if onlyLet:
    print("Your message contains only letters")

print()
print("Task 4")
print()

message = input("Enter your message: ")
if " " in message:
    print("There is spaces in your message")
else:
    print("There is no spaces in your message")

print()
print("Task 5")
print()

message = input("Enter your message: ")
if message.endswith("."):
    print("Your message ends with a dot")
else:
    print("Your message doesn't end with a dot")

print()
print("Task 6")
print()

message = input("Enter your message: ")
for i in message:
    print(i)

print()
print("Task 7")
print()

message = input("Enter your message: ")
counter = 0
for i in message:
    if i.isalpha():
        counter += 1
print(f"Your message has {counter} letters in it")

print()
print("Task 8")
print()

message = input("Enter your message: ")
counter = 0
for i in message:
    if i == " ":
        counter += 1
print(f"Your message has {counter} spaces in it")

print()
print("Task 9")
print()

message = input("Enter your message: ")
for i in range(len(message)):
    if message[i].lower() in "aeiouy":
        print(message[i])

print()
print("Task 10")
print()

message = input("Enter your message: ")
for i in range(len(message)):
    if message[i].lower() in "aeiouy":
        continue
    else:
        print(message[i])

print()
print("Task 11")
print()

message = input("Enter your message: ")
counter = 0

for i in range(len(message)):
    if message[i].lower() == "a":
        counter += 1
print(f"Your message has {counter} A's in it")

print()
print("Task 12")
print()

message = input("Enter your message: ")
counter = 0

for i in range(len(message)):
    if message[i].isupper():
        counter += 1
print(f"Your message contains {counter} capitals")

print()
print("Task 13")
print()

message = input("Enter your message: ")
counter = 0

for i in range(len(message)):
    if message[i].islower():
        counter += 1
print(f"Your message contains {counter} lowercase letters")

print()
print("Task 14")
print()

message = input("Enter your message: ")
counter = 0
for i in message:
    if i.isdigit():
        counter += 1
print(f"Your message has {counter} numbers in it")

print()
print("Task 15")
print()

message = input("Enter your message: ")
numCounter = 0
letCounter = 0

for i in message:
    if i.isdigit():
        numCounter += 1
    elif i.isalpha():
        letCounter += 1
    else:
        continue

if letCounter > numCounter:
    print("You have more letters than numbers in your message")
elif numCounter > letCounter:
    print("You have more numbers than letters in your message")
else:
    print("You have the same amount of numbers and letters")

print()
print("Task 16")
print()

message = input("Enter your message: ")
while message.lower() != "stop":
    message = input("Enter your message: ")

print()
print("Task 17")
print()

message = input("Enter your message: ")
counter = 0

while message.lower() != "0":
    counter += 1
    message = input("Enter your message: ")
print(f"Number of messages: {counter}")

print()
print("Task 18")
print()

message = input("Enter your message: ")
index = len(message) - 1
while index != -1:
    print(message[index])
    index -= 1

print()
print("Task 19")
print()

message = input("Enter your message: ")
resultMessage = ""
index = 0

while index != len(message):
    if message[index] != " ":
        resultMessage += message[index]
    index += 1

print(resultMessage)

print()
print("Task 20")
print()

message = input("Enter your message: ")
resultMessage = ""
index = 0

while index != len(message):
    if message[index].lower() == "a":
        resultMessage += "@"
    else:
        resultMessage += message[index]
    index += 1

print(resultMessage)

print()
print("Task 21")
print()

message = input("Enter your message: ").lower().replace(" ", "")
index = 0
isPolyndrome= True

for i in range(len(message)-1, -1, -1):
    if message[index] == message[i]:
        index += 1
        continue
    else:
        isPolyndrome = False
        break

if isPolyndrome:
    print("Your massage is polyndrome")
else:
    print("Your massage is not polyndrome")

print()
print("Task 22")
print()

message = input("Enter your message: ")
if message.isalpha():
    print("Your message has only letters")
else:
    print("Your message has letters and numbers")

print()
print("Task 23")
print()

message = input("Enter your message: ")
if message.isdigit():
    print("Your message has only numbers")
else:
    print("Your message has letters and numbers")

print()
print("Task 24")
print()

message = input("Enter your message: ")
if len(message) % 2 == 0:
    print(message[0:len(message)//2])
else:
    print(message)

print()
print("Task 25")
print()

message = input("Enter your message: ")
for i in range(0, len(message)):
    if i % 2 != 0:
        print(message[i])

print()
print("Task 26")
print()

message = input("Enter your message: ")
counter = 0
commonSymbol = ""

for char in message:
    if message.count(char) > counter:
        commonSymbol = char
        counter = message.count(char)
print(f"The most common symbol is: {commonSymbol}")

print()
print("Task 27")
print()

message = input("Enter your message: ")
result = ""
index = 0
while index != len(message):
    if message[index] not in result:
        result += message[index]
    index += 1

print(result)

print()
print("Task 28")
print()

message = input("Enter your message: ")
words = message.split()

print(f"Amount of words: {len(words)}")

print()
print("Task 29")
print()

message = input("Enter your message: ")
words = message.split()
for i in range(len(words)):
    words[i] = words[i].capitalize()

for i in words:
    print(i)

print()
print("Task 30")
print()

message = input("Enter your message: ")

for i in range(len(message)):
    if i != len(message) - 1:
        if message[i] == message[i+1]:
            print("You have two symbols in a row")
            break