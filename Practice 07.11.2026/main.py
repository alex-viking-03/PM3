import random

scores = 0
health = 3

for i in range(5):
    if health <= 0:
        print(f"Вы проиграли. У вас не осталось жизней! Вы прошли {i - 1} раундов")
        break
    random_number = random.randint(1, 9)
    user_number = int(input(f'''
=== ОПЕРАЦИЯ "ЧЕРНЫЙ ЯЩИК" ===
Раунд {i+1}/5  жизни: {health}
Черный ящик выдал код: {random_number}
1 - ОТКРЫТЬ
2 - ЗАКРЫТЬ
Твое решение: '''))

    while user_number != 1 and user_number != 2:
        user_number = int(input("Введите 1 или 2! "))

    if random_number % 2 == 1:
        if user_number == 1:
            print("✓ Верно!")
            scores += 1
        else:
            print("✗ Неверно! -1 жизнь")
            health -= 1
    else:
        if user_number == 1:
            print("✗ Неверно! -1 жизнь")
            health -= 1
        else:
            print("✓ Верно!")
            scores += 1

match scores:
    case 0:
        print("Код катастрофический")
    case 1 | 2:
        print("Бункер закрыт!")
    case 3:
        print("Нормально")
    case 4:
        print("Оператор")
    case 5:
        print("Машина")