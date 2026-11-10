user_name = input("Как вас зовут? ")
amount_of_languages = int(input("Сколько язык программирования вы знаете? "))
amount_of_hours = float(input("Сколько часов в неделю вы уделяете в неделю? "))
wanna_be_programmer = input("Вы хотите стать программистом? ")

print(f'''Типы данных:
Имя: {type(user_name)}
Количество языков: {type(amount_of_languages)}
Количество часов: {type(amount_of_hours)}
Ответ на вопрос: {type(wanna_be_programmer)}''')