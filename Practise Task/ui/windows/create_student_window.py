from tkinter import messagebox
import customtkinter as ctk

import database.database as db

class CreateStudentWindow(ctk.CTkToplevel): #Наследуем методы и свойства класса создания окна CTkTopLevel
    def __init__(self, parent, create_student_callback):
        super().__init__(parent)
        self.create_student_callback = create_student_callback

        self.groups = [
            group["name"] for group in db.get_groups()
        ]  #Сокращенный цикл for. Тут мы из списка, который вернется из db.get_groups(), берем именно имя группы и
           #добавляем в список groups

        self.title("Создание студента") #Задаем заголовок окна
        self.geometry("500x200") #Задаем размеры окна

        self.create_form()

    def create_form(self):
        self.columnconfigure(1, weight = 1)

        self.add_name_surname_label = ctk.CTkLabel(
            self,
            text = "ФИО студента: ",
            font = ("Arial", 15, "bold")
        )
        self.add_name_surname_entry = ctk.CTkEntry(
            self,
            placeholder_text = "Введите ФИО студента"
        )

        self.add_name_surname_label.grid(
            row = 0,
            column = 0,
            padx = 20,
            pady = 10,
            sticky = "w"
        )
        self.add_name_surname_entry.grid(
            row = 0,
            column = 1,
            padx = 20,
            pady = 10,
            sticky = "we" #Будет стоять по-середине (между west и east)
        )

        self.add_groups_label = ctk.CTkLabel(
            self,
            text = "Группа: ",
            font = ("Arial", 15, "bold")
        )

        self.add_groups_label.grid(
            row = 1,
            column = 0,
            padx = 20,
            pady = 10,
            sticky = "w"
        )

        self.add_groups_combo = ctk.CTkComboBox( #Создаем виджет, который будет хранить
            self,                                #заранее известные и забитые значения.
            values = self.groups, #Устанавливаем источник значений (группы)
            state = "readonly" #Устанавливаем режим, при котором пользователь не сможет ввести значение вручную
        )

        self.add_groups_combo.grid(
            row = 1,
            column = 1,
            padx = 20,
            pady = 10,
            sticky = "we"
        )

        self.add_button = ctk.CTkButton(
            self,
            text = "Добавить",
            command = self.create
        )

        self.add_button.grid(
            row = 2,
            column = 1,
            padx =20,
            pady = 10,
            sticky = "e"
        )

    def create(self):
        #Получаем данные из полей
        students_name = self.add_name_surname_entry.get()
        students_group = self.add_groups_combo.get()

        #Проверяем его на корректность заполнения
        if students_name.strip() == "":
            messagebox.showerror(
                title = "Ошибка",
                message = "Напишите имя"
            )
            return

        if students_group not in self.groups:
            messagebox.showerror(
                title = "Ошибка",
                message = "Выбрана неправильная группа"
            )
            return

        student = {"name" : students_name,
                   "group" : students_group,
                   "grades" : []}

        self.create_student_callback(student)

        self.destroy()