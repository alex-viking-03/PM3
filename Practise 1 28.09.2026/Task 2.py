counter = 0

for i in range(5):
    num = int(input("Введите число: "))
    if num > 5:
        counter += 1

print(f"Чисел больше 5: {counter}")