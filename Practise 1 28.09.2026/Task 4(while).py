num = int(input("Введите число (желательно побольше символов): "))

counter = 0

while num > 0:
    unit = num % 10
    if unit == 7:
        counter += 1
    num = (num - unit) // 10

print(f'Количество цифр "7" в вашем числе: {counter}')