# Updated DatabaseManager class to include an outstanding balance
import sqlite3
class DatabaseManager:
    def __init__(self, db_name="sis.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.initialize_tables()

    def initialize_tables(self):
        # Create Students table with outstanding_balance
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                first_name TEXT,
                                last_name TEXT,
                                dob TEXT,
                                email TEXT,
                                phone TEXT,
                                outstanding_balance REAL DEFAULT 0)''')  # Add outstanding balance
        
        # Other table definitions remain the same...
        # Create Teachers table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                first_name TEXT,
                                last_name TEXT,
                                email TEXT,
                                expertise TEXT)''')
        
        # Create Courses table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                course_name TEXT,
                                course_code TEXT,
                                teacher_id INTEGER,
                                FOREIGN KEY (teacher_id) REFERENCES teachers(id))''')
        
        # Create Enrollments table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS enrollments (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                student_id INTEGER,
                                course_id INTEGER,
                                enrollment_date TEXT,
                                FOREIGN KEY (student_id) REFERENCES students(id),
                                FOREIGN KEY (course_id) REFERENCES courses(id))''')

        # Create Payments table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS payments (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                student_id INTEGER,
                                amount REAL,
                                payment_date TEXT,
                                FOREIGN KEY (student_id) REFERENCES students(id))''')

        self.connection.commit()

    def close(self):
        self.connection.close()

# SISDatabase class for student and course operations
class SISDatabase:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    # Retrieve a student by student ID
    def get_student_by_id(self, student_id):
        query = "SELECT * FROM students WHERE id = ?"
        self.db_manager.cursor.execute(query, (student_id,))
        return self.db_manager.cursor.fetchone()

    # Insert a new payment
    def record_payment(self, student_id, amount, payment_date):
        query = "INSERT INTO payments (student_id, amount, payment_date) VALUES (?, ?, ?)"
        self.db_manager.cursor.execute(query, (student_id, amount, payment_date))
        self.db_manager.connection.commit()
        return self.db_manager.cursor.lastrowid  # return the ID of the newly inserted payment

    # Update student's outstanding balance
    def update_outstanding_balance(self, student_id, amount):
        query = "UPDATE students SET outstanding_balance = outstanding_balance - ? WHERE id = ?"
        self.db_manager.cursor.execute(query, (amount, student_id))
        self.db_manager.connection.commit()

# Main logic for recording payment for Jane Johnson
if __name__ == "__main__":
    db_manager = DatabaseManager()
    sis_db = SISDatabase(db_manager)

    # Jane Johnson's payment details
    jane_student_id = 101
    payment_amount = 500.00
    payment_date = "2023-04-10"

    # Retrieve Jane's student record
    jane_record = sis_db.get_student_by_id(jane_student_id)

    if jane_record:
        # Record the payment
        payment_id = sis_db.record_payment(jane_student_id, payment_amount, payment_date)
        print(f"Payment of ${payment_amount} recorded for Jane Johnson (Payment ID: {payment_id})")

        # Update Jane's outstanding balance
        sis_db.update_outstanding_balance(jane_student_id, payment_amount)
        print(f"Jane Johnson's outstanding balance has been updated.")
    else:
        print("Student Jane Johnson not found in the system.")

    db_manager.close()
