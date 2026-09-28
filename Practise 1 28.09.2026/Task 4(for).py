num = int(input("Введите число (желательно побольше символов): "))
counter = 0
counter_iterations = 0

num_to_count_iterations = num
while num_to_count_iterations != 0:
    num_to_count_iterations //= 10
    counter_iterations += 1

for i in range(counter_iterations):
    unit = num % 10
    if unit == 7:
        counter += 1
    num = (num - unit) // 10

print(f'Количество цифр "7" в вашем числе: {counter}')