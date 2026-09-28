print("Task 1")
print()

def hello(name):
    return f"Hello, {name}!"

print(hello("Ilya"))

print()
print("Task 2")
print()

def sumOfTwoNums(a,b):
    return a+b

print(sumOfTwoNums(5, 2))

print()
print("Task 3")
print()

def length(lst):
    return len(lst)

print(length([5, 2, 3, 7]))

print()
print("Task 4")
print()

def strLength(string):
    counter = 0
    for i in string:
        if i == " ":
            continue
        else:
            counter += 1
    return counter

print(strLength("Hello, I'm someone"))

print()
print("Task 5")
print()

def maxNum(a, b, c):
    lst = [a, b, c]
    return max(lst)

print(maxNum(5, 2, -5))

print()
print("Task 6")
print()

def oddOrEven(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(oddOrEven(5))

print()
print("Task 7")
print()

def sumOfSomeNums(*nums):
    return sum(nums)
print(sumOfSomeNums(2, 5, 4, 2))

print()
print("Task 8")
print()

def studentsInfo(name, **info):
    result = f"Name: {name},"
    for key, value in info.items():
        result += f" {key}: {value},"
    return result

print(studentsInfo("John", group="A", age=16))

print()
print("Task 9")
print()

def onlyPositive(*nums):
    toReturn = []
    for i in nums:
        if i > 0:
            toReturn.append(i)
    return toReturn

print(onlyPositive(5, 2, -5, 2))

print()
print("Task 10")
print()

def calc(num1, num2, **operations):
    operation = operations.get("operations")
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

print(calc(5, -2, operations="-"))

print()
print("Task 11")
print()

def multiplyTablet(num):
    return (f"{num} * 1 = {num}\n"
            f"{num} * 2 = {num*2}\n"
            f"{num} * 3 = {num*3}\n"
            f"{num} * 4 = {num*4}\n"
            f"{num} * 5 = {num*5}\n"
            f"{num} * 6 = {num*6}\n"
            f"{num} * 7 = {num*7}\n"
            f"{num} * 8 = {num*8}\n"
            f"{num} * 9 = {num*9}\n"
            f"{num} * 10 = {num*10}\n")

print(multiplyTablet(5))

print()
print("Task 12")
print()

def makeMessage(*words):
    return " ".join(words)
print(makeMessage("hello", "world", "me", "you"))

print()
print("Task 13")
print()

students = [("alex", 18), ("egor", 25), ("kolya", 17), ("aron", 4)]
students.sort(key=lambda x: x[1])
print(students)

print()
print("Task 14")
print()

names = ["alex", "egor", "kolya", "aron"]
names2 = list(map(lambda x: x.capitalize(), names))
print(names2)

print()
print("Task 15")
print()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

print()
print("Task 16")
print()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squaredNums = list(map(lambda x: x ** 2, nums))
print(squaredNums)

print()
print("Task 17")
print()

emails = ["douffunnaugiyo-2874@yopmail.com", "nofugrennibau-2393@yopmail.com", "diriyegeivou-8758@yopmail.com"]
sortedEmails = list(sorted(emails, key=lambda x: len(x), reverse=False))
print(sortedEmails)

print()
print("Task 18")
print()

def make_multiplier(n):
    def second_num(m):
        return m * n
    return second_num

times3 = make_multiplier(3)
print(times3(10))

print()
print("Task 19")
print()

def hello_lang(language):
    def hello_name(name):
        if language == "en":
            return f"Hello, {name}"
        elif language == "ru":
            return f"Привет, {name}"
        else:
            return "No such language"
    return hello_name

hello = hello_lang("ru")
print(hello("Alex"))

print()
print("Task 20")
print()

def counter():
    count = 0
    def count_iteration():
        nonlocal count
        count += 1
        return count
    return count_iteration

programmCounter = counter()
print(programmCounter())
print(programmCounter())

print()
print("Task 21")
print()

def rememberList():
    lst = []
    def addNumToList(num):
        nonlocal lst
        lst.append(num)
        return lst
    return addNumToList

ourList = rememberList()
print(ourList(4))
print(ourList(6))

print()
print("Task 22")
print()

def create_account(begginCapital):
    balance = begginCapital
    def operation(oper, money):
        nonlocal balance
        if oper == "deposit":
            balance += money
            print(balance)
        elif oper == "withdraw":
            if balance > money:
                balance -= money
                print(balance)
            else:
                print("Error")
        else:
            print("No such operation")
    return operation

account = create_account(20)
account("deposit", 10)
account("withdraw", 5)
account("withdraw", 50)

print()
print("Task 23")
print()

def create_logger():
    logs = []
    def logger(message):
        logs.append(message)
        return logs
    def get_logs():
        return logs.copy()
    return logger, get_logs

log, get_logs = create_logger()
log("Hello")
log("Shit")
print(get_logs())

print()
print("Task 24")
print()

class Student:
    def __init__(self, name, age, group):
        self.name = name
        self.age = age
        self.group = group
    def info(self):
        return f"Name: {self.name}\nAge: {self.age}\nGroup: {self.group}"

student1 = Student("Alex", 18, "207")
student2 = Student("Aron", 17, "208")

print(student1.info())
print()
print(student2.info())

print()
print("Task 25")
print()

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.height = length
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 *(self.width + self.height)

rectangle1 = Rectangle(5, 6 )
rectangle2 = Rectangle(4, 10)

print(rectangle1.area())
print(rectangle1.perimeter())
print()
print(rectangle2.area())
print(rectangle2.perimeter())

print()
print("Task 26")
print()

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Error")
    def get_balance(self):
        return self.balance

my_account = BankAccount(100)

my_account.withdraw(200)
print(my_account.get_balance())

print()
print("Task 27")
print()

class Customer:
    def __init__(self, customerId, firstName, lastName, company, city, country, phone1, phone2, email, subscriptionDate, website):
        self.customerId = customerId
        self.FirstName = firstName
        self.LastName = lastName
        self.Company = company
        self.City = city
        self.Country = country
        self.Phone1 = phone1
        self.Phone2 = phone2
        self.Email = email
        self.SubscriptionDate = subscriptionDate
        self.Website = website

    def show_info(self):
        print(f"Customer Id: {self.customerId}\n"
              f"First Name: {self.FirstName}\n"
              f"Last Name: {self.LastName}\n"
              f"Company: {self.Company}\n"
              f"City: {self.City}\n"
              f"Country: {self.Country}\n"
              f"Phone 1: {self.Phone1}\n"
              f"Phone 2: {self.Phone2}\n"
              f"Email: {self.Email}\n"
              f"Subscription Date: {self.SubscriptionDate}\n"
              f"Website: {self.Website}\n")

customer1 = Customer("1Ef7b82A4CAAD10", "Preston", "Lozano",
                     "Vega-Gentry","East Jimmychester", "Djibouti",
                     "+5153435776", "686-620-1820-944", "vmata@colon.com",
                     "2021-04-23", "http://www.hobbs.com/")
customer1.show_info()

print()
print("Task 28")
print()

class EmailValidator:
    def __init__(self, email):
        self.email = email

    def valid_email(self):
        return ("@" in self.email and
                "." in self.email and
                self.email.count("@") == 1)

    def has_domein(self):
        try:
            return bool(self.email.split("@", 1)[1])
        except Exception:
            return False

    def is_corporate(self):
        if self.has_domein():
            if self.email.split("@")[1] in ["gmail.com", "yahoo.com", "outlook.com"]:
                return True
            else:
                return False
        else:
            return False

email_validator = EmailValidator("beckycarr@@gmail.com")
print(email_validator.valid_email())
print(email_validator.has_domein())
print(email_validator.is_corporate())

print()
print("Task 29")
print()

class CRM:
    def __init__(self, customers):
        self.customers = customers

    def filter_by_country(self, country):
        filtered = []
        for customer in self.customers:
            if customer.get("country") == country:
                filtered.append(customer)
        return filtered

    def add_customer(self, customer):
        self.customers.append(customer)

    def top_domains(self, n):
        domain_counter = {}
        for customer in self.customers:
            email = customer.get("email", "")
            if "@" in email:
                domain = email.split("@", 1)[1].lower()

                if domain in domain_counter:
                    domain_counter[domain] += 1
                else:
                    domain_counter[domain] = 1

        sorted_domains = sorted(domain_counter.items(), key=lambda x: x[1], reverse=True)
        return sorted_domains[:n]

customers = [
    {"name": "Alice", "email": "alice@gmail.com", "country": "USA"},
    {"name": "Bob", "email": "bob@company.com", "country": "USA"},
    {"name": "Eva", "email": "eva@yahoo.com", "country": "Germany"},
    {"name": "Max", "country": "Germany"},
]

crm = CRM(customers)
crm.add_customer({
    "name": "John",
    "email": "john@company.com",
    "country": "USA"
})
print(crm.filter_by_country("Germany"))
print(crm.top_domains(3))