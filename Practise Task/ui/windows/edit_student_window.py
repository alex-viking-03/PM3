from tkinter import messagebox
import database.database as db
import customtkinter as ctk


class EditStudentWindow(ctk.CTkToplevel):
    def __init__(self, parent, student, edit_callback):
        super().__init__(parent)
        self.edit_callback = edit_callback
        self.groups = [
            group["name"] for group in db.get_groups()
        ] #Сокращенный цикл for. Тут мы из списка, который вернется из db.get_groups(), берем именно имя группы и
           #добавляем в список groups

        self.title("Редактировать студента") #Задаем заголовок окна
        self.geometry("500x400") #Задаем размеры окна

        self.student = student
        self.create_form()

    def create_form(self):
        self.columnconfigure(1, weight=1)

        self.name_surname_label = ctk.CTkLabel(
            self,
            text = "ФИО студента: "
        )
        self.name_surname_entry = ctk.CTkEntry(
            self,
            placeholder_text = "Введите ФИО"
        )

        self.name_surname_label.grid(
            row = 0,
            column = 0,
            padx = 20,
            pady = 10
        )
        self.name_surname_entry.grid(
            row = 0,
            column = 1,
            padx = 20,
            pady = 10,
            sticky = "ew"
        )
        self.name_surname_entry.insert(0, self.student["name"])

        self.group_name_label = ctk.CTkLabel(
            self,
            text = "Группа: "
        )
        self.group_name_combo = ctk.CTkComboBox( #Создаем виджет, который будет хранить
            self,                                #заранее известные и забитые значения.
            values = self.groups, #Устанавливаем источник значений (группы)
            state = "readonly" #Устанавливаем режим, при котором пользователь не сможет ввести значение вручную
        )

        self.group_name_label.grid(
            row = 1,
            column = 0,
            padx = 20,
            pady = 10
        )
        self.group_name_combo.grid(
            row = 1,
            column = 1,
            padx = 20,
            pady = 10,
            sticky = "ew"
        )
        self.group_name_combo.set(self.student["group"]) #Заполняем значение поля имеющейся группой студента из базы

        self.save_button = ctk.CTkButton(
            self,
            text = "Сохранить",
            command = self.save_edition
        )
        self.save_button.grid(
            row = 2,
            column = 1,
            padx = 20,
            pady = 10
        )

    def save_edition(self):
        #Получаем значения из полей
        name_surname = self.name_surname_entry.get().strip()
        group_name = self.group_name_combo.get()

        #Проверяем их на корректность
        if name_surname == "":
            messagebox.showerror(
                title = "Ошибка",
                message = "Введено некорректное ФИО"
            )
            return

        if group_name not in self.groups:
            messagebox.showerror(
                title="Ошибка",
                message="Введена некорректная Группа"
            )
            return

        result = messagebox.askyesno(
            "Изменение",
            "Сохранить изменения?"
        )

        #Сохраняем
        if result:
            self.student["group"] = group_name
            self.student["name"] = name_surname
            self.edit_callback()

        self.destroy()