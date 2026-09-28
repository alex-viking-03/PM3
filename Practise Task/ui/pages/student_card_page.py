from tkinter import messagebox

import customtkinter as ctk
import database.database as db

from ui.windows.add_grade_window import AddGradeWindow
from ui.windows.edit_student_window import EditStudentWindow


class StudentCardPage(ctk.CTkFrame):
    def __init__(self, parent, student, back_callback, delete_callback):
        super().__init__(parent) #Запускаем конструктор класса CTkFrame

        self.student = student
        self.back_callback = back_callback
        self.delete_callback = delete_callback

        self.create_back_button()
        self.create_header()
        self.create_info_box()
        self.create_grades_box()

    def create_back_button(self):
        self.back_button = ctk.CTkButton(
            self,
            text = "<-- Назад",
            command = self.back_callback
        )

        self.back_button.pack(
            padx = 20,
            pady = 10,
            anchor = "w"
        )

    def create_header(self):
        self.student_card_header = ctk.CTkFrame(self)
        self.student_card_header.pack(
            fill = "x",
            padx = 20,
            pady = 10
        )
        self.student_card_header.grid_columnconfigure( #Выставляем приоритет колонки. Указанная колонка будет занимать большее место
            0,
            weight = 1
        )

        self.name_label = ctk.CTkLabel(
            self.student_card_header,
            text = self.student["name"],
            font = ("Arial", 20)
        )
        self.name_label.grid( #Выставляем наш виджет на позицию сетки
            row = 0, #Строка 0
            column = 0, #Колонка 0
            padx = 20,
            pady = 10,
            sticky = "w" #Текст будет находится ближе к левому краю (w = west)
        )

        self.header_group_label = ctk.CTkLabel(
            self.student_card_header,
            text = f"Группа: {self.student["group"]}",
            font = ("Arial", 20)
        )
        self.header_group_label.grid( #Выставляем наш виджет на позицию сетки
            row = 1, #Строка 1
            column = 0, #Колонка 0
            padx = 20,
            pady = 10,
            sticky = "w" #Текст будет находится ближе к левому краю (w = west)
        )

        self.average_label = ctk.CTkLabel(
            self.student_card_header,
            text = f"Средний балл: {self.calculate_average()}",
            font = ("Arial", 20)
        )

        self.average_label.grid( #Выставляем наш виджет на позицию сетки
            row = 1, #Строка 1
            column = 1, #Колонка 1
            padx = 20,
            pady = 10,
            sticky = "e" #Текст будет находиться ближе к правому краю (e = east)
        )

    def create_info_box(self):
        self.info_box = ctk.CTkFrame(self)
        self.info_box.grid_columnconfigure(
            0,
            weight = 1
        )
        self.info_box.pack(
            fill = "x",
            padx = 20,
            pady = 10
        )

        self.info_header_label = ctk.CTkLabel(
            self.info_box,
            text = "Информация о студенте"
        )

        self.info_header_label.grid(
            row = 0,
            column = 0,
            padx = 20,
            pady = 10,
            sticky = "w"
        )

        self.name_surname_label = ctk.CTkLabel(
            self.info_box,
            text = f"ФИО: {self.student['name']}"
        )
        self.name_surname_label.grid(
            row = 1,
            column = 0,
            padx = 20,
            pady = (10, 0),
            sticky = "w"
        )

        self.info_group_label = ctk.CTkLabel(
            self.info_box,
            text=f"Группа: {self.student['group']}"
        )
        self.info_group_label.grid(
            row=2,
            column=0,
            padx=20,
            pady = (0, 10),
            sticky = "w"
        )

        self.delete_button = ctk.CTkButton(
            self.info_box,
            text = "Удалить студента",
            command = self.delete_student
        )
        self.delete_button.grid(
            row = 0,
            column = 2,
            padx = 20,
            pady = 10,
            sticky = "e"
        )

        self.edit_button = ctk.CTkButton(
            self.info_box,
            text = "Редактировать",
            command = self.open_edit_student_window
        )
        self.edit_button.grid(
            row = 0,
            column = 1,
            padx = 20,
            pady = 10,
            sticky = "e"
        )

    def create_grades_box(self):
        self.grades_box = ctk.CTkFrame(self)
        self.grades_box.pack(
            fill = "both",
            expand = True,
            padx = 20,
            pady = 10
        )
        self.grades_box.grid_columnconfigure(
            0,
            weight = 1
        )

        self.grades_header_label = ctk.CTkLabel(
            self.grades_box,
            text = "Оценки"
        )

        self.grades_header_label.grid(
            row = 0,
            column = 0,
            padx = 20,
            pady = 10,
            sticky = "w"
        )

        self.add_grade_button = ctk.CTkButton(
            self.grades_box,
            text = "Добавить оценку",
            command = self.open_add_grade_window
        )
        self.add_grade_button.grid(
            row = 0,
            column = 3,
            padx = 20,
            pady = 10,
            sticky = "e"
        )

        self.subject_header = ctk.CTkLabel(
            self.grades_box,
            text = "Предмет",
            font = ("Arial", 15, "bold")
        )
        self.grade_header = ctk.CTkLabel(
            self.grades_box,
            text = "Оценка",
            font = ("Arial", 15, "bold")
        )
        self.date_header = ctk.CTkLabel(
            self.grades_box,
            text = "Дата",
            font = ("Arial", 15, "bold")
        )

        self.subject_header.grid(
            row = 1,
            column = 0,
            padx = 20,
            pady = 10,
            sticky = "w"
        )
        self.grade_header.grid(
            row = 1,
            column = 1,
            padx = 20,
            pady = 10
        )
        self.date_header.grid(
            row = 1,
            column = 2,
            padx = 20,
            pady = 10
        )
        self.draw_grades()


    def draw_grades(self):
        for row_index, grade in enumerate(self.student['grades'], start = 2):
            subject_label = ctk.CTkLabel(
                self.grades_box,
                text = grade['subject']
            )

            grade_label = ctk.CTkLabel(
                self.grades_box,
                text = grade['grade']
            )

            date_label = ctk.CTkLabel(
                self.grades_box,
                text = grade['date']
            )

            delete_button = ctk.CTkButton(
                self.grades_box,
                text = "Удалить",
                command = lambda g=grade: self.delete_grade(g) #Назначаем лямбда функцию и туда передаем g.
                                                               #Это нужно для того, чтобы функция не исполнилась сразу
                                                               #как только код дошел до этой точки
            )

            subject_label.grid(
                row = row_index,
                column = 0,
                padx = 20,
                pady = 5,
                sticky = "w"
            )

            grade_label.grid(
                row = row_index,
                column = 1,
                padx = 20,
                pady = 5
            )

            date_label.grid(
                row = row_index,
                column = 2,
                padx = 20,
                pady = 5
            )

            delete_button.grid(
                row = row_index,
                column = 3,
                padx = 20,
                pady = 5
            )

    def calculate_average(self):
        grades = self.student['grades']

        if len(grades) == 0:
            return 0

        total = 0

        for grade in grades:
            total += grade['grade']

        return round(total / len(grades), 2)

    def open_add_grade_window(self):
        AddGradeWindow(
            self,
            self.add_grade
        )

    def add_grade(self, grade):
        grade_id = db.add_grade(
            grade,
            self.student["id"]
        )

        grade["id"] = grade_id
        self.student['grades'].append(grade)

        self.clear_grades()
        self.draw_grades()
        self.update_average()

    def clear_grades(self):
        for widget in self.grades_box.winfo_children():
            grid_info = widget.grid_info()

            if grid_info and int(grid_info["row"]) >= 2:
                widget.destroy()

    def update_average(self):
        average = self.calculate_average()
        self.average_label.configure(text = f"Средний балл: {str(average)}")

    def open_edit_student_window(self):
        EditStudentWindow(
            self,
            self.student,
            self.save_edition
        )

    def save_edition(self):
        db.update_student(self.student)

        self.update_header()
        self.update_info()

    def update_header(self):
        self.name_label.configure(
            text = self.student['name']
        )

        self.header_group_label.configure(
            text = f"Группа: {self.student['group']}"
        )

    def update_info(self):
        self.name_surname_label.configure(
            text = f"ФИО: {self.student['name']}"
        )
        self.info_group_label.configure(
            text = f"Группа: {self.student['group']}"
        )

    def delete_grade(self, grade):
        result = messagebox.askyesno(
            "Удаление оценки",
            f'Удалить оценку {grade["grade"]} по предмету "{grade["subject"]}"'
        )

        if not result:
            return

        db.delete_grade(grade["id"])
        self.student["grades"].remove(grade)

        self.clear_grades()
        self.draw_grades()
        self.update_average()

    def delete_student(self):
        result = messagebox.askyesno(
            "Удаление студента",
            "Вы уверена, что хотите удалить студента?"
        )

        if result:
            self.delete_callback(self.student)