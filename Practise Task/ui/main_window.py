import customtkinter as ctk
from database import database

from ui.pages.student_card_page import StudentCardPage
from ui.pages.students_page import StudentsPage
from ui.pages.groups_page import GroupsPage
from ui.pages.subjects_page import SubjectsPage
from ui.windows.create_student_window import CreateStudentWindow


class MainWindow(ctk.CTk):  #Наследуем свойства и методы класса CTk библиотеки CustomTkinter
    def __init__(self): #Конструктор
        super().__init__() #Прогоняем конструктор наследуемого класса

        self.students = database.get_students() #В собственную переменную students сохраняем студентов из БД

        self.title("Менеджер студентов") #Задаем заголовок окна
        self.geometry("1200x700") #Задаем размеры окна

        # Вызываем собственные методы создания контейнеров, в который будут храниться наши виджеты
        self.create_sidebar()
        self.create_content()

    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(    #Создаем собственный контейнер sidebar
            self, #Родителем является само окно приложения
            width = 200, #Ширина
            corner_radius = 0 #Закругление углов
        )

        self.sidebar.pack( #Размещаем наш контейнер
            side = "left", #Прижимаем к левой стороне
            fill = "y" #Растягиваем по высоте окна (y = сторона в системе координат)
        )

        self.students_button = ctk.CTkButton( #Создаем кнопку
            self.sidebar, #Родителем выступает созданный нами ранее контейнер
            text = "Студенты", #Текст кнопки
            command = self.show_students_page #Команда, которая исполнится при нажатии на кнопку
        )

        self.students_button.pack( #Размещаем
            padx = 5, #Отступаем по 5 с каждой стороны по горизонтали
            pady = 20 #Отступаем по 20 с каждой стороны по вертикали
        )

        self.groups_button = ctk.CTkButton(
            self.sidebar,
            text = "Группы",
            command = self.show_groups_page
        )

        self.groups_button.pack(
            padx = 20
        )

        self.subjects_button = ctk.CTkButton(
            self.sidebar,
            text = "Предметы",
            command = self.show_subjects_page
        )

        self.subjects_button.pack(
            padx = 20,
            pady = 20
        )

    def create_content(self):
        self.content = ctk.CTkFrame(self)
        self.content.pack(
            side = "right",
            fill = "both", #Растягиваем уже и по х, и по у
            expand = True, #Забираем все оставшееся свободное пространство окна
            padx = 10,
            pady = 10
        )

        self.students_page = StudentsPage( #Открываем в этом контейнере окно StudentsPage
            self.content,
            self.students,
            self.open_student_card,
            self.open_create_student
        )

        self.students_page.pack(
            fill = "both",
            expand = True
        )

    def show_students_page(self):
        self.students = database.get_students()

        self.clear_content()

        self.students_page = StudentsPage(
            self.content,
            self.students,
            self.open_student_card,
            self.open_create_student
        )

        self.students_page.pack(
            fill = "both",
            expand = True
        )

    def clear_content(self):
        for widget in self.content.winfo_children(): #Получаем информацию о каждом виджете в контейнере content
            widget.destroy() #Уничтожаем его

    def show_groups_page(self):
        self.clear_content()

        self.groups_page = GroupsPage(self.content)
        self.groups_page.pack(
            fill = "both",
            expand = True
        )

    def open_student_card(self, student):
        self.clear_content()
        self.student_card_page = StudentCardPage(
            self.content,
            student,
            self.show_students_page,
            self.delete_student
        )

        self.student_card_page.pack(
            fill = "both",
            expand = True
        )

    def delete_student(self, student):
        database.delete_student(student["id"])
        self.show_students_page()

    def open_create_student(self):
        CreateStudentWindow(
            self,
            self.create_student
        )

    def create_student(self, student):
        database.add_student(student)
        self.show_students_page()

    def show_subjects_page(self):
        self.clear_content()

        self.subjects_page = SubjectsPage(self.content)

        self.subjects_page.pack(
            fill = "both",
            expand = True
        )