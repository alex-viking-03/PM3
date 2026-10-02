from database import get_connection
from datetime import date
from decimal import Decimal, InvalidOperation
import calendar

def get_subscriptions(user_id):
    conn = get_connection()

    try:
        subscriptions = conn.execute(
            """
            SELECT *
            FROM subscription
            WHERE user_id = ?
            ORDER BY next_payment, id
            """,
            (user_id,)
        ).fetchall()

        return subscriptions
    finally:
        conn.close()

def add_subscription(user_id, name, amount_text, period, next_payment):
    name, amount, payment_date = validate_subscription(
        name, amount_text, period, next_payment
    )

    conn = get_connection()

    try:
        with conn:
            conn.execute(
                """
                INSERT INTO subscription (
                    user_id, name, amount, period,
                    next_payment, payment_day
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    name,
                    amount,
                    period,
                    payment_date.isoformat(),
                    payment_date.day
                )
            )
    finally:
        conn.close()

def update_subscription(
    user_id, subscription_id, name,
    amount_text, period, next_payment
):
    name, amount, payment_date = validate_subscription(
        name, amount_text, period, next_payment
    )

    conn = get_connection()

    try:
        with conn:
            old_subscription = conn.execute(
                """
                SELECT next_payment, payment_day
                FROM subscription
                WHERE id = ? AND user_id = ?
                """,
                (subscription_id, user_id)
            ).fetchone()

            if old_subscription is None:
                raise ValueError("Подписка не найдена.")

            # При изменении только названия или цены
            # сохраняем исходный день оплаты.
            if payment_date.isoformat() == old_subscription["next_payment"]:
                payment_day = old_subscription["payment_day"]
            else:
                payment_day = payment_date.day

            conn.execute(
                """
                UPDATE subscription
                SET name = ?, amount = ?, period = ?,
                    next_payment = ?, payment_day = ?
                WHERE id = ? AND user_id = ?
                """,
                (
                    name, amount, period,
                    payment_date.isoformat(), payment_day,
                    subscription_id, user_id
                )
            )
    finally:
        conn.close()

def validate_subscription(name, amount_text, period, next_payment):
    name = name.strip()

    if not name:
        raise ValueError("Введи название подписки.")

    try:
        amount = Decimal(amount_text.strip().replace(",", "."))
    except InvalidOperation:
        raise ValueError("Введи корректную стоимость.") from None

    if not amount.is_finite() or amount <= 0:
        raise ValueError("Стоимость должна быть больше нуля.")

    if amount > Decimal("1000000000"):
        raise ValueError("Стоимость слишком большая.")

    if amount != amount.quantize(Decimal("0.01")):
        raise ValueError("Укажи не больше двух знаков после запятой.")

    if period not in ("monthly", "yearly"):
        raise ValueError("Выбери период оплаты.")

    try:
        payment_date = date.fromisoformat(next_payment.strip())
    except ValueError:
        raise ValueError("Некорректная дата оплаты.") from None

    return name, int(amount * 100), payment_date

def delete_subscription(user_id, subscription_id):
    conn = get_connection()

    try:
        with conn:
            cursor = conn.execute(
                """
                DELETE FROM subscription
                WHERE id = ? AND user_id = ?
                """,
                (subscription_id, user_id)
            )

            if cursor.rowcount == 0:
                raise ValueError("Подписка не найдена.")
    finally:
        conn.close()

def get_next_payment(current_date, period, payment_day):
    if period == "monthly":
        year = current_date.year
        month = current_date.month + 1

        if month > 12:
            month = 1
            year += 1

    elif period == "yearly":
        year = current_date.year + 1
        month = current_date.month

    else:
        raise ValueError("Неизвестный период оплаты.")

    if year > 9999:
        raise ValueError("Невозможно перенести дату дальше.")

    # Узнаём количество дней в новом месяце.
    days_in_month = calendar.monthrange(year, month)[1]

    # Если исходного дня нет, берём последний день месяца.
    day = min(payment_day, days_in_month)

    return date(year, month, day)

def mark_paid(user_id, subscription_id):
    conn = get_connection()

    try:
        with conn:
            subscription = conn.execute(
                """
                SELECT *
                FROM subscription
                WHERE id = ? AND user_id = ?
                """,
                (subscription_id, user_id)
            ).fetchone()

            if subscription is None:
                raise ValueError("Подписка не найдена.")

            current_date = date.fromisoformat(
                subscription["next_payment"]
            )

            new_date = get_next_payment(
                current_date,
                subscription["period"],
                subscription["payment_day"]
            )

            conn.execute(
                """
                UPDATE subscription
                SET next_payment = ?
                WHERE id = ? AND user_id = ?
                """,
                (new_date.isoformat(), subscription_id, user_id)
            )
    finally:
        conn.close()

def calculate_expenses(subscriptions):
    yearly_total = 0

    for subscription in subscriptions:
        if subscription["period"] == "monthly":
            yearly_total += subscription["amount"] * 12
        else:
            yearly_total += subscription["amount"]

    # Переводим тиыны в тенге.
    yearly = Decimal(yearly_total) / 100
    monthly = yearly / 12

    return monthly, yearly

def get_payment_status(next_payment, today=None):
    if today is None:
        today = date.today()

    payment_date = date.fromisoformat(next_payment)
    days_left = (payment_date - today).days

    if days_left < 0:
        return "overdue", f"Просрочено на {abs(days_left)} дн."

    if days_left == 0:
        return "today", "Оплата сегодня"

    if days_left <= 7:
        return "soon", f"Через {days_left} дн."

    return "later", f"До оплаты {days_left} дн."