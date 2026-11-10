stuff_name = input("Введите имя товара: ")
stuff_price = float(input("Введите цену товара: "))
stuff_amount = int(input("Введите количество товаров: "))

total_amount = stuff_amount * stuff_price

print(f'''
Имя товара: {stuff_name}
Цена товара: {stuff_price}
Количество товара: {stuff_amount}
Итоговая стоимость: {total_amount}''')