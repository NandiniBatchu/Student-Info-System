import sqlite3

class DatabaseManager:
    def __init__(self, db_name="sis.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.initialize_tables()

    def initialize_tables(self):
        # Create Students table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                first_name TEXT,
                                last_name TEXT,
                                dob TEXT,
                                email TEXT,
                                phone TEXT)''')
        
        # Create Teachers table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                first_name TEXT,
                                last_name TEXT,
                                email TEXT)''')
        
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

class SISDatabase:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def insert_student(self, first_name, last_name, dob, email, phone):
        query = "INSERT INTO students (first_name, last_name, dob, email, phone) VALUES (?, ?, ?, ?, ?)"
        self.db_manager.cursor.execute(query, (first_name, last_name, dob, email, phone))
        self.db_manager.connection.commit()
    
    def update_student(self, student_id, first_name, last_name, dob, email, phone):
        query = '''UPDATE students
                   SET first_name = ?, last_name = ?, dob = ?, email = ?, phone = ?
                   WHERE id = ?'''
        self.db_manager.cursor.execute(query, (first_name, last_name, dob, email, phone, student_id))
        self.db_manager.connection.commit()

    def insert_enrollment(self, student_id, course_id, enrollment_date):
        query = "INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (?, ?, ?)"
        self.db_manager.cursor.execute(query, (student_id, course_id, enrollment_date))
        self.db_manager.connection.commit()

    def insert_payment(self, student_id, amount, payment_date):
        query = "INSERT INTO payments (student_id, amount, payment_date) VALUES (?, ?, ?)"
        self.db_manager.cursor.execute(query, (student_id, amount, payment_date))
        self.db_manager.connection.commit()

    def get_student_by_id(self, student_id):
        query = "SELECT * FROM students WHERE id = ?"
        self.db_manager.cursor.execute(query, (student_id,))
        return self.db_manager.cursor.fetchone()

    def get_enrollments_for_student(self, student_id):
        query = '''SELECT courses.course_name, enrollments.enrollment_date
                   FROM enrollments
                   JOIN courses ON enrollments.course_id = courses.id
                   WHERE enrollments.student_id = ?'''
        self.db_manager.cursor.execute(query, (student_id,))
        return self.db_manager.cursor.fetchall()
    
    def get_courses_for_teacher(self, teacher_id):
        query = '''SELECT courses.course_name
                   FROM courses
                   WHERE courses.teacher_id = ?'''
        self.db_manager.cursor.execute(query, (teacher_id,))
        return self.db_manager.cursor.fetchall()
    def enroll_student_in_course(self, student_id, course_id, enrollment_date):
        try:
            self.db_manager.connection.execute("BEGIN")
            self.insert_enrollment(student_id, course_id, enrollment_date)
            # Any other related operations can go here
            self.db_manager.connection.commit()
        except Exception as e:
            self.db_manager.connection.rollback()
            raise Exception(f"Transaction failed: {e}")
class QueryBuilder:
    def __init__(self):
        self.query = ""
        self.params = []

    def select(self, table, columns="*"):
        self.query = f"SELECT {columns} FROM {table}"
        return self
    
    def where(self, column, condition, value):
        self.query += f" WHERE {column} {condition} ?"
        self.params.append(value)
        return self
    
    def order_by(self, column, direction="ASC"):
        self.query += f" ORDER BY {column} {direction}"
        return self
    
    def build(self):
        return self.query, tuple(self.params)
    
class SISQueryHandler:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def execute_query(self, query_builder):
        query, params = query_builder.build()
        self.db_manager.cursor.execute(query, params)
        return self.db_manager.cursor.fetchall()
query_builder = QueryBuilder().select("students").where("dob", ">", "2000-01-01").order_by("last_name")
sis_query_handler = SISQueryHandler(db_manager)
students = sis_query_handler.execute_query(query_builder)

for student in students:
    print(student)
