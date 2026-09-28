num = int(input("Введите число: "))

if num <= 0:
    print("Введено неверное число. Число должно быть больше нуля")

for i in range(num, 0, -1):
    if i % 3 == 0:
        print("ТРИ")
    else:
        print(i)