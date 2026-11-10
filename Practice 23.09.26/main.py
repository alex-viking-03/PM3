def even_or_not(number):
    if number == 0:
        return "Zero"
    elif number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_not(int(input("Enter number: "))))