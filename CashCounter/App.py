import customtkinter as ctk
import sqlite3
from tkinter import messagebox

from auth import *
from subscriptions import *
from ui.subscription_add import SubscriptionWindow

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cash Counter")
        self.geometry("460x350")
        self.resizable(width=False, height=False)

        self.current_user = None

        self.show_login()

    def show_login(self):
        self.clear_window()
        self.geometry("460x350")
        self.resizable(width=False, height=False)

        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=25, pady=25)

        ctk.CTkLabel(
            frame,
            text="Cash counter",
            font = ctk.CTkFont(size=24, weight="bold")
        ).pack(pady=(20,15))

        self.username_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Логин",
            width=320
        )
        self.username_entry.pack(pady=8)

        self.password_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Пароль",
            show="*",
            width=320
        )
        self.password_entry.pack(pady=8)

        self.status_label = ctk.CTkLabel(
            frame,
            text=""
        )
        self.status_label.pack(pady=5)

        buttons = ctk.CTkFrame(frame, fg_color="transparent")
        buttons.pack(pady=10)

        ctk.CTkButton(
            buttons,
            text="Войти",
            width=140,
            command=self.login
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            buttons,
            text="Зарегистрироваться",
            width=180,
            command=self.register
        ).pack(side="left", padx=5)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            register_user(username, password)

        except ValueError as e:
            self.show_error(str(e))
            return

        except sqlite3.Error:
            self.show_error("Не удалось сохранить аккаунт")
            return

        self.status_label.configure(
            text="Аккаунт создан. Теперь нажми «Войти».",
            text_color="green"
        )

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            user = login(username, password)

        except ValueError as e:
            self.show_error(str(e))
            return


        except sqlite3.Error as error:
            print(f"Ошибка SQLite: {error}")
            self.show_error(str(error))
            return

        self.current_user = user
        self.show_main()


    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_error(self, text):
        self.status_label.configure(
            text=text,
            text_color="red"
        )

    def show_main(self):
        self.clear_window()

        self.geometry("900x600")
        self.resizable(True, True)

        top_bar = ctk.CTkFrame(self)
        top_bar.pack(fill="x", padx=20, pady=20)

        ctk.CTkLabel(
            top_bar,
            text=f"Привет, {self.current_user['username']}!",
            font=ctk.CTkFont(size=22, weight="bold")
        ).pack(side="left", padx=15, pady=15)

        ctk.CTkButton(
            top_bar,
            text="Выйти",
            command=self.logout
        ).pack(side="right", padx=15)

        ctk.CTkButton(
            self,
            text="Добавить подписку",
            command=self.open_add_subscription
        ).pack(anchor="w", padx=20, pady=(0, 10))

        self.expenses_label = ctk.CTkLabel(
            self,
            text="",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.expenses_label.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        self.subscriptions_frame = ctk.CTkScrollableFrame(self)
        self.subscriptions_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.refresh_subscriptions()

    def logout(self):
        self.current_user = None
        self.show_login()

    def refresh_subscriptions(self):\

        for widget in self.subscriptions_frame.winfo_children():
            widget.destroy()

        try:
            subscriptions = get_subscriptions(self.current_user["id"])
        except sqlite3.Error as error:
            ctk.CTkLabel(
                self.subscriptions_frame,
                text=f"Ошибка загрузки: {error}",
                text_color="red"
            ).pack(pady=20)
            return

        monthly, yearly = calculate_expenses(subscriptions)

        self.expenses_label.configure(
            text=(
                f"В среднем за месяц: {monthly:,.2f} ₸"
                f"    |    За год: {yearly:,.2f} ₸"
            )
        )

        if not subscriptions:
            ctk.CTkLabel(
                self.subscriptions_frame,
                text="У тебя пока нет подписок."
            ).pack(pady=20)
            return

        for subscription in subscriptions:
            row = ctk.CTkFrame(self.subscriptions_frame)
            row.pack(fill="x", pady=5)

            ctk.CTkButton(
                row,
                text="Удалить",
                width=90,
                fg_color="#a83232",
                hover_color="#802626",
                command=lambda sub_id=subscription["id"]: self.remove_subscription(sub_id)
            ).pack(side="right", padx=10, pady=10)

            ctk.CTkButton(
                row,
                text="Изменить",
                width=90,
                command=lambda sub=subscription: self.open_edit_subscription(sub)
            ).pack(side="right", padx=5, pady=10)

            # Переводим тиыны в тенге для отображения.
            amount = subscription["amount"] / 100

            period = (
                "месяц"
                if subscription["period"] == "monthly"
                else "год"
            )

            ctk.CTkLabel(
                row,
                text=subscription["name"]
            ).pack(side="left", padx=15, pady=10)

            ctk.CTkLabel(
                row,
                text=f"{amount:.2f} ₸ / {period}"
            ).pack(side="left", padx=15)

            ctk.CTkLabel(
                row,
                text=f"Следующая оплата: {subscription['next_payment']}"
            ).pack(side="right", padx=15)

            ctk.CTkButton(
                row,
                text="Оплачено",
                width=90,
                command=lambda sub_id=subscription["id"]: self.pay_subscription(sub_id)
            ).pack(side="right", padx=5, pady=10)

            status, status_text = get_payment_status(
                subscription["next_payment"]
            )

            colors = {
                "overdue": "#ff6b6b",
                "today": "#ffb347",
                "soon": "#ffd166",
                "later": "#a0a0a0"
            }

            ctk.CTkLabel(
                row,
                text=status_text,
                text_color=colors[status]
            ).pack(side="right", padx=10)



    def open_add_subscription(self):
        SubscriptionWindow(
            master=self,
            user_id=self.current_user["id"],
            on_saved=self.refresh_subscriptions
        )

    def remove_subscription(self, subscription_id):
        confirmed = messagebox.askyesno(
            "Удаление подписки",
            "Удалить эту подписку?",
            parent=self
        )

        if not confirmed:
            return

        try:
            delete_subscription(
                self.current_user["id"],
                subscription_id
            )
        except (ValueError, sqlite3.Error) as error:
            messagebox.showerror(
                "Ошибка удаления",
                str(error),
                parent=self
            )
            return

        self.refresh_subscriptions()

    def pay_subscription(self, subscription_id):
        confirmed = messagebox.askyesno(
            "Оплата подписки",
            "Подтвердить оплату за один период?",
            parent=self
        )

        if not confirmed:
            return

        try:
            mark_paid(
                self.current_user["id"],
                subscription_id
            )
        except (ValueError, sqlite3.Error) as error:
            messagebox.showerror(
                "Ошибка",
                str(error),
                parent=self
            )
            return

        self.refresh_subscriptions()

    def open_edit_subscription(self, subscription):
        SubscriptionWindow(
            master=self,
            user_id=self.current_user["id"],
            on_saved=self.refresh_subscriptions,
            subscription=subscription
        )