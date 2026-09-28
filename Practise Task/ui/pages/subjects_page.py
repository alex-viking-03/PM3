from tkinter import messagebox

import customtkinter as ctk
import database.database as db


class SubjectsPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.subjects = db.get_subjects()

        self.create_title()
        self.create_top_bar()
        self.create_subjects_list()

        self.draw_subjects(self.subjects)

    def create_title(self):
        self.title_label = ctk.CTkLabel(
            self,
            text="Предметы",
            font=("Arial", 28)
        )

        self.title_label.pack(
            padx=20,
            pady=(20, 10),
            anchor="w"
        )

    def create_top_bar(self):
        self.top_bar = ctk.CTkFrame(self)

        self.top_bar.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.search_var = ctk.StringVar()
        self.search_var.trace_add(
            "write",
            self.search_subjects
        )

        self.search_entry = ctk.CTkEntry(
            self.top_bar,
            placeholder_text="Поиск предмета...",
            textvariable=self.search_var
        )

        self.search_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        self.add_button = ctk.CTkButton(
            self.top_bar,
            text="Добавить предмет",
            command=self.open_add_subject_dialog
        )

        self.add_button.pack(side="right")

    def create_subjects_list(self):
        self.subjects_list = ctk.CTkFrame(self)

        self.subjects_list.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.subjects_list.grid_columnconfigure(
            0,
            weight=1
        )

        self.name_header = ctk.CTkLabel(
            self.subjects_list,
            text="Название предмета",
            font=("Arial", 18, "bold")
        )

        self.name_header.grid(
            row=0,
            column=0,
            padx=20,
            pady=10,
            sticky="w"
        )

        self.action_header = ctk.CTkLabel(
            self.subjects_list,
            text="Действие",
            font=("Arial", 18, "bold")
        )

        self.action_header.grid(
            row=0,
            column=1,
            padx=20,
            pady=10
        )

    def draw_subjects(self, subjects):
        self.clear_subjects()

        for row_index, subject in enumerate(subjects, start=1):
            name_label = ctk.CTkLabel(
                self.subjects_list,
                text=subject["name"]
            )

            name_label.grid(
                row=row_index,
                column=0,
                padx=20,
                pady=10,
                sticky="w"
            )

            delete_button = ctk.CTkButton(
                self.subjects_list,
                text="Удалить",
                width=90,
                command=lambda s=subject: self.delete_subject(s)
            )

            delete_button.grid(
                row=row_index,
                column=1,
                padx=20,
                pady=10
            )

    def clear_subjects(self):
        for widget in self.subjects_list.winfo_children():
            grid_info = widget.grid_info()

            if grid_info and int(grid_info["row"]) >= 1:
                widget.destroy()

    def search_subjects(self, *args):
        search_text = self.search_var.get().strip().casefold()

        filtered_subjects = [
            subject
            for subject in self.subjects
            if search_text in subject["name"].casefold()
        ]

        self.draw_subjects(filtered_subjects)

    def open_add_subject_dialog(self):
        dialog = ctk.CTkInputDialog(
            title="Добавление предмета",
            text="Введите название предмета:"
        )

        subject_name = dialog.get_input()

        if subject_name is None:
            return

        try:
            db.add_subject(subject_name)
        except ValueError as error:
            messagebox.showerror(
                title="Ошибка",
                message=str(error)
            )
            return

        self.refresh_subjects()

    def delete_subject(self, subject):
        result = messagebox.askyesno(
            title="Удаление предмета",
            message=f'Удалить предмет "{subject["name"]}"?'
        )

        if not result:
            return

        db.delete_subject(subject["id"])
        self.refresh_subjects()

    def refresh_subjects(self):
        self.subjects = db.get_subjects()
        self.search_var.set("")
        self.draw_subjects(self.subjects)