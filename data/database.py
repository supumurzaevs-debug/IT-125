import sqlite3


class Database:
    def __init__(self, db_name="students.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE,
            last_name TEXT,
            first_name TEXT,
            middle_name TEXT,
            birth_date TEXT,
            phone TEXT,
            email TEXT,
            group_name TEXT,
            major TEXT,
            course INTEGER,
            study_form TEXT
        )
        """)
        self.connection.commit()

    def add_student(self, data):
        self.cursor.execute("""
        INSERT INTO students (
            telegram_id, last_name, first_name, middle_name,
            birth_date, phone, email, group_name,
            major, course, study_form
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
        self.connection.commit()

    def student_exists(self, telegram_id):
        self.cursor.execute("SELECT 1 FROM students WHERE telegram_id = ?", (telegram_id,))
        return self.cursor.fetchone() is not None
