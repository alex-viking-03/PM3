import sqlite3
import sys
from pathlib import Path

if getattr(sys, 'frozen', False): #Программа запускается .ехе или .ру
    BASE_DIR = Path(sys.executable).resolve().parent #Берем путь исполняемого файла, конвертируем его в тип данных Path,
                                                     #переводим в абсолютный путь и берем путь родительской папки
else:
    BASE_DIR = Path(__file__).resolve().parent #Конвертируем путь к ТЕКУЩЕМУ файлу в Path и делаем все то же,
                                               # что в if = True

DB_NAME = BASE_DIR / "students.db" #Собираем путь


def get_connection():
    conn = sqlite3.connect(DB_NAME) #Подключаемся к базе с путем DB_NAME. Если базы там не будет, она создастся
    conn.row_factory = sqlite3.Row #Даем возможность обращаться к данным из базы по имени столбца
    conn.execute("PRAGMA foreign_keys = ON") #Включаем контроль связей таблиц
    return conn

def create_tables():
    with get_connection() as conn: #С подключением, который нам вернул get_connection() выполняем следующий блок кода
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                group_name TEXT NOT NULL 
            )
        """) #Если не существует, создаем таблицу students. id - целочисленный ключ, который
             #генерирует порядковый номер автоматически. name - ФИО студента, текст, не пустой.
             #group_name - название группы студента, текст, не пустой

        conn.execute("""
            CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                subject TEXT NOT NULL,
                grade INTEGER NOT NULL CHECK (grade BETWEEN 1 AND 5),
                date TEXT NOT NULL,
                
                FOREIGN KEY (student_id)
                    REFERENCES students (id)
                    ON DELETE CASCADE
            )
        """) #Тут отличие от таблицы выше с том, что grade проверяет, что значение
             #находится в диапазоне между 1 и 5, и в конце мы устанавливаем связь с таблицей students.
             #В students_id мы записываем ключ, который есть в таблице students под полем id

        conn.execute("""
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)

        conn.executemany(
            """
            INSERT OR IGNORE INTO groups (name)
            VALUES (?)
            """,
            [
                ("СД-104",),
                ("СД-204",),
                ("СД-304",),
                ("СД-404",)
            ]
        ) #Здесь отличие в том, что в groups мы добавляем значения из parameters,
          #.executemany() делает то же, что если бы мы несколько раз написали обычный .execute() с разными параметрами

        conn.execute("""
            CREATE TABLE IF NOT EXISTS subjects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)

        conn.executemany(
            """
            INSERT OR IGNORE INTO subjects (name)
            VALUES (?)
            """,
            [
                ("Математика",),
                ("Программирование",),
                ("Физика",)
            ]
        )

def get_students():
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT 
                id,
                name,
                group_name
            FROM students
            ORDER BY name
        """).fetchall()

    students = []

    for row in rows:
        grade_rows = conn.execute("""
            SELECT
                id,
                subject,
                grade,
                date
            FROM grades
            WHERE student_id = ?
            ORDER BY date DESC
        """, (row["id"],)).fetchall()

        grades = []

        for grade_row in grade_rows:
            grades.append({
                "id": grade_row["id"],
                "subject": grade_row["subject"],
                "grade": grade_row["grade"],
                "date": grade_row["date"]
            })

        students.append({
            "id": row["id"],
            "name": row["name"],
            "group": row["group_name"],
            "grades": grades
        })

    return students

def add_student(student):
    with get_connection() as conn:
        cursor = conn.execute("""
            INSERT INTO students (
                name,
                group_name
            )
            VALUES (?, ?)
        """, (
            student["name"],
            student["group"]
        ))

        return cursor.lastrowid

def delete_student(student_id):
    with get_connection() as conn:
        cursor = conn.execute("""
            DELETE FROM students
            WHERE id = ?
            """,
            (student_id,)
        )

def add_grade(grade, student_id):
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO grades (
                student_id,
                subject,
                grade,
                date
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                student_id,
                grade["subject"],
                grade["grade"],
                grade["date"]
            )
        )

        return cursor.lastrowid

def delete_grade(grade_id):
    with get_connection() as conn:
        cursor = conn.execute(
            """
            DELETE FROM grades
            WHERE id = ?
            """,
            (grade_id,)
        )

def update_student(student):
    with get_connection() as conn:
        conn.execute(
            """
            UPDATE students
            SET
                name = ?,
                group_name = ?
            WHERE id = ?
            """,
            (student["name"],
                       student["group"],
                       student["id"])
        )

def get_groups():
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT id, name
            FROM groups
            ORDER BY name
        """).fetchall()

    return [dict(row) for row in rows]

def add_group(name):
    name = name.strip()

    if not name:
        raise ValueError("Введите имя группы")

    try:
        with get_connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO groups (name)
                VALUES (?)
                """,
                (name,)
            )

            return cursor.lastrowid #lastrowid = Значение, которое хранится в нашем cursor
    except sqlite3.IntegrityError:
        raise ValueError("Такая группа уже существует")

def delete_group(group_id):
    with get_connection() as conn:
        conn.execute(
            """
            DELETE FROM groups
            WHERE id = ?
            """,
            (group_id,)
        )

def get_subjects():
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT id, name
            FROM subjects
            ORDER BY name
        """).fetchall()

    return [dict(row) for row in rows]

def add_subject(name):
    name = name.strip()

    if not name:
        raise ValueError("Введите название предмета")

    try:
        with get_connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO subjects (name)
                VALUES (?)
                """,
                (name,)
            )

            return cursor.lastrowid
    except sqlite3.IntegrityError:
        raise ValueError("Такой предмет уже существует")

def delete_subject(subject_id):
    with get_connection() as conn:
        conn.execute(
            """
            DELETE FROM subjects
            WHERE id = ?
            """,
            (subject_id,)
        )