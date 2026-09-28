import customtkinter as ctk

class StudentsPage(ctk.CTkFrame):
    def __init__(self, parent, students, open_student_callback, open_create_student_callback):
        super().__init__(parent)
        self.students = students
        self.open_student_callback = open_student_callback
        self.open_create_student_callback = open_create_student_callback

        self.title_label = ctk.CTkLabel(
            self,
            text='Студенты',
            font=('Arial', 28)
        )

        self.title_label.pack(
            padx = 20,
            pady = (20, 10),
            anchor = 'w'
        )

        self.top_bar = ctk.CTkFrame(self)
        self.top_bar.pack(
            fill = 'x',
            padx = 20,
            pady = 10
        )

        self.search_var = ctk.StringVar()
        self.search_var.trace_add(
            "write",
            self.search_students
        )

        self.search_entry = ctk.CTkEntry(
            self.top_bar,
            placeholder_text = "Поиск студента....",
            textvariable = self.search_var
        )

        self.search_entry.pack(
            side = 'left',
            fill = 'x',
            expand = True,
            padx = (0, 10)
        )

        self.add_button = ctk.CTkButton(
            self.top_bar,
            text = "Добавить студента",
            command = open_create_student_callback
        )

        self.add_button.pack(
            side = "right"
        )

        self.students_list = ctk.CTkFrame(self)

        self.students_list.pack(
            fill = 'both',
            expand = True,
            padx = 20,
            pady = (0, 20)
        )

        self.name_header = ctk.CTkLabel(
            self.students_list,
            text = "ФИО",
            font = ("Arial", 18, "bold")
        )

        self.group_header = ctk.CTkLabel(
            self.students_list,
            text = "Группа",
            font = ("Arial", 18, "bold")
        )

        self.average_header = ctk.CTkLabel(
            self.students_list,
            text = "Средний балл",
            font = ("Arial", 18, "bold")
        )

        self.action_header = ctk.CTkLabel(
            self.students_list,
            text = "Действие",
            font = ("Arial", 18, "bold")
        )

        self.name_header.grid(
            row = 0,
            column = 0,
            padx = 20,
            pady = 10,
            sticky = 'w'
        )

        self.group_header.grid(
            row = 0,
            column = 1,
            padx = 20,
            pady = 10
        )

        self.average_header.grid(
            row = 0,
            column = 2,
            padx = 20,
            pady = 10
        )

        self.action_header.grid(
            row = 0,
            column = 3,
            padx = 20,
            pady = 10
        )

        self.students_list.grid_columnconfigure(
            0,
            weight = 1
        )

        self.draw_students(self.students)

    def draw_students(self, students):
        self.clear_students()

        for row_index, student in enumerate(students, start = 1):
            name_label = ctk.CTkLabel(
                self.students_list,
                text = student["name"]
            )
            group_label = ctk.CTkLabel(
                self.students_list,
                text = student["group"]
            )
            average_label = ctk.CTkLabel(
                self.students_list,
                text = str(self.calculate_average(student))
            )

            open_button = ctk.CTkButton(
                self.students_list,
                text = "Открыть",
                width = 90,
                command = lambda s=student: self.open_student(s)
            )

            name_label.grid(
                row = row_index,
                column = 0,
                padx = 20,
                pady = 10,
                sticky = 'w'
            )

            group_label.grid(
                row = row_index,
                column = 1,
                padx = 20,
                pady = 10
            )

            average_label.grid(
                row = row_index,
                column = 2,
                padx = 20,
                pady = 10
            )

            open_button.grid(
                row = row_index,
                column = 3,
                padx = 20,
                pady = 10
            )

    def open_student(self, student):
        self.open_student_callback(student)

    def calculate_average(self, student):
        grades = student["grades"]

        if len(grades) == 0:
            return 0

        total = 0

        for grade in grades:
            total += grade["grade"]

        return round(total / len(grades), 2)

    def clear_students(self):
        for widget in self.students_list.winfo_children():
            grid_info = widget.grid_info()

            if grid_info and int(grid_info["row"]) >= 1:
                widget.destroy()

    def search_students(self, *args):
        search_text = self.search_var.get().strip().casefold()

        filtered_students = []

        for student in self.students:
            student_name = student["name"].casefold()
            student_group = student["group"].casefold()

            if (
                search_text in student_name
                or search_text in student_group
            ):
                filtered_students.append(student)

        self.draw_students(filtered_students)