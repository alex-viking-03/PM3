# print("Task 1")
# print()
#
# people = {"Artem": 24, "Ilya": 24, "Alex": 17, "Aron": 16}
# print(people)
# people["Artem"] = 25
# print(people)
# for key, value in people.items():
#     if value >= 18:
#         print(f"{key.capitalize()} is {value} years old")
#
# print()
# print("Task 2")
# print()
#
# goods = {"Apple": 200, "Honey": 150, "Flour": 210, "Cola": 350}
# expensiveProduct = None
# expensivePrice = 0
#
# for key, value in goods.items():
#     if value > expensivePrice:
#         expensivePrice = value
#         expensiveProduct = key
# print(f"The most expensive product is {expensiveProduct}: {expensivePrice}")
#
# print()
# print("Task 3")
# print()
#
# subjects = {"Math": 90, "PE": 100, "Physics": 80, "Chemistry": 60}
# counter = 0
# for key, value in subjects.items():
#     counter += value
#
# print(f"Average grade: {counter/len(subjects)}")
#
# print()
# print("Task 4")
# print()
#
# city = {"city1": 18000, "city2": 58476, "city3": 190349, "city4": 2170, "city5": 100493}
# for key, value in city.items():
#     if value >= 100000:
#         print(key.capitalize())
#
# print()
# print("Task 5")
# print()
#
# grade = {"Alex": 94, "Kolya": 80, "Alisher":81, "Aron": 75}
# minValue = max(grade.values())
# name = None
#
# for key, value in grade.items():
#     if value <= minValue:
#         name = key.capitalize()
# print(f"{name}: {grade[name]}")
#
# print()
# print("Task 6")
# print()
#
# def print_numbers(n):
#     for i in range(1, n+1):
#         print(i)
#
# length = int(input("How many numbers do you want? "))
# print_numbers(length)
#
# print()
# print("Task 7")
# print()
#
# def sum_list(lst):
#     return sum(lst)
#
# numbers = [1, 6, 3, 6 ,4, 1, 8]
# print(f"Sum of all values in list: {sum_list(numbers)}")
#
# print()
# print("Task 8")
# print()
#
# def max_in_list(lst):
#     maxValue = lst[0]
#     for i in lst:
#         if i > maxValue:
#             maxValue = i
#     return maxValue
#
# lst = [4, 3, 2, 9, 6, -158, 98, 4, 3456]
# print("Max value in list: ", max_in_list(lst))
#
# print()
# print("Task 9")
# print()
#
# def count_even(lst):
#     evenCount = 0
#     for i in lst:
#         if i % 2 == 0:
#             evenCount += 1
#     return evenCount
#
# listOfNumbers = [1, 6, 3, 6, 4, 1, 8]
# print("Amount of even numbers in list:", count_even(listOfNumbers))
#
# print()
# print("Task 10")
# print()
#
# def is_sorted(lst):
#     for i in range(len(lst) - 1):
#         if lst[i] > lst[i + 1]:
#             return False
#     return True
#
# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# list2 = [1, 2, 3, 4, 4, 8, 2, 4, 3]
#
# print(f"Is list1 sorted?: {is_sorted(list1)}\n"
#       f"Is list2 sorted?: {is_sorted(list2)}")
#
# print()
# print("Task 11")
# print()
#
# def print_dict(d):
#     for key, value in d.items():
#         print(f"{key}: {value}")
#
# subjects = {"Math": 90, "PE": 100, "Physics": 80, "Chemistry": 60}
# print_dict(subjects)
#
# print()
# print("Task 12")
# print()
#
# def average_value(dic):
#     total = 0
#     for value in dic.values():
#         total += value
#     return total / len(dic)
#
# subjects = {"Math": 90, "PE": 100, "Physics": 80, "Chemistry": 60}
# average_value(subjects)
#
# print()
# print("Task 13")
# print()
#
# def max_key(d):
#     maxKey = None
#     maxValue = max(d.values())
#     for key in d.keys():
#         if d[key] == maxValue:
#             maxKey = key
#     return maxKey
#
# city = {"city1": 18000, "city2": 58476, "city3": 190349, "city4": 2170, "city5": 100493}
# print(f"Key with max value: {max_key(city)}")
#
# print()
# print("Task 14")
# print()
#
# def filter_dict(d, x):
#     newDict = {}
#     for key, value in d.items():
#         if value >= x:
#             newDict[key] = value
#     return newDict
#
# city = {"city1": 18000, "city2": 58476, "city3": 190349, "city4": 2170, "city5": 100493}
# print(f"New dict: {filter_dict(city, 100000)}")
#
# print()
# print("Task 15")
# print()
#
# def count_adults(dict):
#     adults = {}
#     for key, value in dict.items():
#         if value >= 18:
#             adults[key] = value
#     return adults
#
# people = {"Artem": 24, "Ilya": 24, "Alex": 17, "Aron": 16}
# print(f"Number of people with adults: {count_adults(people)}")
#
# print()
# print("Task 16")
# print()
#
# def average_grades(dic):
#     averageGradesDict = {}
#     for key, value in dic.items():
#         averageGradesDict[key] = sum(value) / len(dic[key])
#     return averageGradesDict
#
# grade = {"Alex": [94, 80, 95, 60], "Kolya": [80, 65, 90, 85], "Alisher":[81, 98, 75, 86], "Aron": [75, 86, 90, 75]}
# averageGrades = average_grades(grade)
# print(averageGrades)
#
# print()
# print("Task 17")
# print()
#
# def top_3(dic):
#     top3Dic = {}
#     for product, price in dic.items():
#         if len(top3Dic) < 3:
#             top3Dic[product] = price
#         else:
#             min_product = None
#             min_price = max(top3Dic.values())
#
#             for p, pr in top3Dic.items():
#                 if pr < min_price:
#                     min_product = p
#                     min_price = pr
#
#             if price > min_price:
#                 del top3Dic[min_product]
#                 top3Dic[product] = price
#     return top3Dic
#
# goods = {"Apple": 200, "Honey": 150, "Flour": 210, "Cola": 350}
# print(top_3(goods))
#
# print()
# print("Task 18")
# print()
#
# def more_then_average(dic):
#     averageGradesDict = {}
#
#     for key, value in dic.items():
#         if value >= sum(dic.values()) / len(dic):
#             averageGradesDict[key] = [value]
#
#     return averageGradesDict
#
#
# grade = {"Alex": 94, "Kolya": 80, "Alisher":86, "Aron": 65}
# dictOfGrades = more_then_average(grade)
# for key, value in dictOfGrades.items():
#     print(f"{key}: {value}")
#
# print()
# print("Task 19")
# print()
#
# def max_sum(dic):
#     maxTotal = 0
#     daysKey = ""
#     for key, value in dic.items():
#         if maxTotal < sum(value):
#             maxTotal = sum(value)
#             daysKey = key
#     return {daysKey: maxTotal}
#
# days = {"Monday": [4, 34, 2], "Tuesday": [58, 50, 11], "Wednesday": [65, 48, 30]}
# sumOfDays = max_sum(days)
# print(sumOfDays)
#
# print()
# print("Task 20")
# print()
#
# def is_mature(dic):
#     adultsDic = {}
#     for key, value in dic.items():
#         if value >= 18:
#             adultsDic[key] = value
#     return adultsDic
#
# people = {"Artem": 24,  "Alex": 17, "Ilya": 24,"Aron": 16}
# print(f"Number of adult people:")
# adults = is_mature(people)
#
# for key, value in adults.items():
#     print(f"{key}: {value}")
#
# def hello(nm):
#     print("hello",nm)
# name = input()
# hello(name)


def af(a,d):
    return a+d
b = int(input())
af(b,7)
