import sqlite3
from datetime import date

import customtkinter as ctk
import tkcalendar as tkc
from subscriptions import add_subscription, update_subscription
from decimal import Decimal


class SubscriptionWindow(ctk.CTkToplevel):
    def __init__(self, master, user_id, on_saved, subscription=None):
        super().__init__(master)

        self.user_id = user_id
        self.on_saved = on_saved
        self.subscription = subscription

        self.title(
            "Редактирование подписки"
            if subscription is not None
            else "Добавление подписки"
        )

        self.geometry("420x420")
        self.resizable(False, False)
        self.transient(master)


        ctk.CTkLabel(
            self,
            text=(
                "Редактирование подписки"
                if subscription is not None
                else "Новая подписка"
            ),
            font=ctk.CTkFont(size=22, weight="bold")
        ).pack(pady=(20, 15))

        self.name_entry = ctk.CTkEntry(
            self,
            placeholder_text="Название подписки",
            width=320
        )
        self.name_entry.pack(pady=8)

        self.amount_entry = ctk.CTkEntry(
            self,
            placeholder_text="Стоимость в тенге",
            width=320
        )
        self.amount_entry.pack(pady=8)

        self.period_box = ctk.CTkComboBox(
            self,
            values=["Каждый месяц", "Каждый год"],
            state="readonly",
            width=320
        )
        self.period_box.set("Каждый месяц")
        self.period_box.pack(pady=8)

        ctk.CTkLabel(
            self,
            text="Следующая оплата"
        ).pack(pady=(8, 0))

        self.date_entry = tkc.DateEntry(
            self,
            date_pattern="dd.mm.yyyy",
            firstweekday="monday",
            width=27,
            font=("Arial", 12),
            background="#1f6aa5",
            foreground="white",
            borderwidth=2,
            state="readonly"
        )
        self.date_entry.pack(pady=8)

        self.status_label = ctk.CTkLabel(
            self,
            text="",
            text_color="red",
            wraplength=350
        )
        self.status_label.pack(pady=5)

        ctk.CTkButton(
            self,
            text="Сохранить",
            command=self.save
        ).pack(pady=10)

        # Захватываем ввод, когда окно появится.
        self.after(100, self.activate)

        if self.subscription is not None:
            self.name_entry.insert(0, self.subscription["name"])

            amount = Decimal(self.subscription["amount"]) / 100
            self.amount_entry.insert(0, f"{amount:.2f}")

            self.period_box.set(
                "Каждый месяц"
                if self.subscription["period"] == "monthly"
                else "Каждый год"
            )

            self.date_entry.set_date(
                date.fromisoformat(self.subscription["next_payment"])
            )

    def activate(self):
        self.grab_set()
        self.name_entry.focus_set()

    def save(self):
        periods = {
            "Каждый месяц": "monthly",
            "Каждый год": "yearly"
        }

        try:
            data = {
                "user_id": self.user_id,
                "name": self.name_entry.get(),
                "amount_text": self.amount_entry.get(),
                "period": periods[self.period_box.get()],
                "next_payment": self.date_entry.get_date().isoformat()
            }

            if self.subscription is None:
                add_subscription(**data)
            else:
                update_subscription(
                    subscription_id=self.subscription["id"],
                    **data
                )

        except ValueError as error:
            self.status_label.configure(text=str(error))
            return
        except sqlite3.Error as error:
            print(f"Ошибка SQLite: {error}")
            self.status_label.configure(
                text="Не удалось сохранить подписку."
            )
            return

        self.destroy()
        self.on_saved()