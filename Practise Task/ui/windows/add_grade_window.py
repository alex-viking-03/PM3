from tkinter import messagebox
import database.database as db
import customtkinter as ctk
import tkcalendar as tkc
from datetime import datetime

class AddGradeWindow(ctk.CTkToplevel): #Наследуем методы и свойства класса создания окна CTkTopLevel
    def __init__(self, parent, save_callback):
        super().__init__(parent)
        self.subjects = [
            subject["name"] for subject in db.get_subjects()
        ] #Сокращенный цикл for. В нём мы перебираем полученные из db.get_subjects() предметы
          #и добавляем их названия в собственный список self.subjects

        self.grades_variants = [str(i) for i in range(1, 6)]
        #В этом сокращенном цикле мы перебираем числа от 1 до 5, конвертируем их в строку
        #и добавляем строчные значения в собственный список self.grades_variants

        self.save_callback = save_callback

        self.title("Добавить оценку") #Устанавливаем заголовок окна
        self.geometry("400x300") #Устанавливаем размеры окна

        self.create_form()

    def create_form(self):
        self.subject_combo = ctk.CTkComboBox( #Создаем виджет, который будет хранить
            self,                             #заранее известные и забитые значения.
            values = self.subjects, #Устанавливаем источник значений (предметов)
            state = "readonly" #Устанавливаем режим, при котором пользователь не сможет ввести значение вручную
        )
        self.subject_combo.pack(
            fill = "x",
            padx = 20,
            pady = 10
        )

        self.grade_combo = ctk.CTkComboBox( #Создаем виджет, который будет хранить
            self,                           #заранее известные и забитые значения.
            values = self.grades_variants, #Устанавливаем источник значений (оценок)
            state = "readonly" #Устанавливаем режим, при котором пользователь не сможет ввести значение вручную
        )
        self.grade_combo.pack(
            fill = "x",
            padx = 20,
            pady = 10
        )

        self.date_entry = tkc.DateEntry( #Создаём виджет, который позволит нам выбрать дату из календаря
            self,
            date_pattern = "dd.mm.yyyy", #Задаем формат даты
            font = ("Arial", 15),
        )
        self.date_entry.pack(
            fill = "x",
            padx = 20,
            pady = 10
        )

        self.save_button = ctk.CTkButton(
            self,
            text = "Сохранить",
            command = self.save_grade
        )
        self.save_button.pack(
            padx = 20,
            pady = 20
        )

    def save_grade(self):
        #Получаем значения из всех полей и сохраняем их в соответствующие переменные
        subject = self.subject_combo.get()
        grade_text = self.grade_combo.get()
        date = self.date_entry.get()

        #Проверяем данные на корректность
        if grade_text not in self.grades_variants:
            messagebox.showerror(
                "Ошибка",
                "Выбрана неверная оценка"
            )
            return

        if subject not in self.subjects:
            messagebox.showerror(
                "Ошибка",
                "Выбран неверный предмет"
            )
            return

        if not self.date_is_valid(date):
            messagebox.showerror(
                "Ошибка",
                "Выбрана неверная дата"
            )
            return

        #Собираем список, в виде которого хранится одна оценка в таблице
        grade = {
            "subject" : subject,
            "grade" : int(grade_text),
            "date" : date
        }

        result = messagebox.askyesno(
            "Выставление оценки",
            "Вы уверены, что хотите выставить эту оценку?"
        )
        if result:
            self.save_callback(grade)

        self.destroy()

    #Проверка даты на корректность
    def date_is_valid(self, date):
        try:
            datetime.strptime(date, "%d.%m.%Y") #Эта конвертирует строку в дату и таким
            return True                                #образом проверить даже такие значения как 30
                                                       #февраля или 13 месяц и т.п.
        except ValueError:
            return False