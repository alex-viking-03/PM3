from tkinter import messagebox

import customtkinter as ctk
import database.database as db

class GroupsPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) #Запускаем конструктор класса CTkFrame

        self.groups = db.get_groups()

        self.create_title()
        self.create_top_bar()
        self.create_groups_list()

        self.draw_groups(self.groups)

    def create_title(self):
        self.title_label = ctk.CTkLabel(
            self,
            text="Группы",
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

        self.search_var = ctk.StringVar() #Специальный тип данных строки, позволяющий связываться с интерфейсом
        self.search_var.trace_add( #Устанавливаем слежку за переменной search_var в режиме "письма.
            "write", #Это означает: "Если в этой переменной добавятся или удалятся символы, запускай это функцию"
            self.search_groups #Функция, которая запускается при изменениях
        )

        self.search_entry = ctk.CTkEntry(
            self.top_bar,
            placeholder_text="Поиск группы...",
            textvariable=self.search_var #Устанавливаем переменную, куда будет динамично сохранятся ввод
        ) #Такой связкой мы обеспечили обновление списка сразу после того, как в строку поиска будут вводить текст поиска

        self.search_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        self.add_button = ctk.CTkButton(
            self.top_bar,
            text="Добавить группу",
            command=self.open_add_group_dialog
        )

        self.add_button.pack(side="right")

    def create_groups_list(self):
        self.groups_list = ctk.CTkFrame(self)

        self.groups_list.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.groups_list.grid_columnconfigure( #Выставляем приоритет колонки. Указанная колонка будет занимать большее место
            0,
            weight=1
        )

        self.name_header = ctk.CTkLabel(
            self.groups_list,
            text="Название группы",
            font=("Arial", 18, "bold")
        )

        self.name_header.grid( #Выставляем наш виджет на позицию сетки
            row=0, #Строка 0
            column=0, #Колонка 0
            padx=20,
            pady=10,
            sticky="w" #Текст будет находится ближе к левому краю (w = west)
        )

        self.action_header = ctk.CTkLabel(
            self.groups_list,
            text="Действие",
            font=("Arial", 18, "bold")
        )

        self.action_header.grid( #Выставляем наш виджет на позицию сетки
            row=0, #Строка 0
            column=1, #Колонка 1
            padx=20,
            pady=10
        )

    def draw_groups(self, groups):
        self.clear_groups()

        for row_index, group in enumerate(groups, start=1):
            name_label = ctk.CTkLabel(
                self.groups_list,
                text=group["name"]
            )

            name_label.grid(
                row=row_index,
                column=0,
                padx=20,
                pady=10,
                sticky="w"
            )

            delete_button = ctk.CTkButton(
                self.groups_list,
                text="Удалить",
                width=90,
                command=lambda g=group: self.delete_group(g)
            )

            delete_button.grid(
                row=row_index,
                column=1,
                padx=20,
                pady=10
            )

    def clear_groups(self):
        for widget in self.groups_list.winfo_children():
            grid_info = widget.grid_info() #Получаем информацию о строке нахождения виджета

            if grid_info and int(grid_info["row"]) >= 1:
                widget.destroy()

    def search_groups(self, *args):
        search_text = self.search_var.get().strip().casefold()

        filtered_groups = [
            group
            for group in self.groups
            if search_text in group["name"].casefold() #Перевод всех символов в нижний регистр
        ] #Эта краткая функции for и проверки if. В ней мы сначала проверяем, находится ли наш search_text
          #в имени группы приведенном в нижний регистр. Если истина, то добавляем его в filtered_groups. Все это происходит
          #в цикле for

        self.draw_groups(filtered_groups)

    def open_add_group_dialog(self):
        dialog = ctk.CTkInputDialog(
            title="Добавление группы",
            text="Введите название группы:"
        ) #Разница обычного окна и этого диалогового в том, что этот диалог представляет из себя
          #готовое окно с вопросом, полем ввода и кнопками готовности или отмены

        group_name = dialog.get_input() #Получаем введенное значение после закрытия диалога

        if group_name is None:
            return

        try:
            db.add_group(group_name)
        except ValueError as error:
            messagebox.showerror(
                title="Ошибка",
                message=str(error)
            )
            return

        self.refresh_groups()

    def delete_group(self, group):
        result = messagebox.askyesno(
            title="Удаление группы",
            message=f'Удалить группу "{group["name"]}"?'
        ) #Небольшое окошко с вопросов да или нет (например, для вопроса закрыть форму или нет)

        if not result:
            return

        db.delete_group(group["id"])
        self.refresh_groups()

    def refresh_groups(self):
        self.groups = db.get_groups()
        self.search_var.set("")
        self.draw_groups(self.groups)