# SISDatabase class with methods to handle student creation and course enrollment

class SISDatabase:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def insert_student(self, first_name, last_name, dob, email, phone):
        query = "INSERT INTO students (first_name, last_name, dob, email, phone) VALUES (?, ?, ?, ?, ?)"
        self.db_manager.cursor.execute(query, (first_name, last_name, dob, email, phone))
        self.db_manager.connection.commit()
        return self.db_manager.cursor.lastrowid  # return the ID of the newly inserted student
    
    def get_course_by_name(self, course_name):
        query = "SELECT id FROM courses WHERE course_name = ?"
        self.db_manager.cursor.execute(query, (course_name,))
        return self.db_manager.cursor.fetchone()

    def insert_course(self, course_name, course_code, teacher_id=None):
        query = "INSERT INTO courses (course_name, course_code, teacher_id) VALUES (?, ?, ?)"
        self.db_manager.cursor.execute(query, (course_name, course_code, teacher_id))
        self.db_manager.connection.commit()
        return self.db_manager.cursor.lastrowid  # return the ID of the newly inserted course

    def insert_enrollment(self, student_id, course_id, enrollment_date):
        query = "INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (?, ?, ?)"
        self.db_manager.cursor.execute(query, (student_id, course_id, enrollment_date))
        self.db_manager.connection.commit()

# Assuming you already have an instance of the DatabaseManager created
db_manager = DatabaseManager()

sis_db = SISDatabase(db_manager)

# Insert John Doe's information into the students table
john_doe_id = sis_db.insert_student("John", "Doe", "1995-08-15", "john.doe@example.com", "123-456-7890")
print(f"John Doe has been added to the system with student ID: {john_doe_id}")

# Enroll John in 'Introduction to Programming' and 'Mathematics 101'
courses = [
    {"course_name": "Introduction to Programming", "course_code": "CS101"},
    {"course_name": "Mathematics 101", "course_code": "MATH101"}
]

for course in courses:
    # Check if the course already exists in the database
    course_id = sis_db.get_course_by_name(course["course_name"])
    
    # If the course doesn't exist, insert it
    if not course_id:
        course_id = sis_db.insert_course(course["course_name"], course["course_code"])
        print(f"Added course {course['course_name']} with course ID: {course_id}")
    else:
        course_id = course_id[0]  # course_id is a tuple, so we need to get the ID

    # Enroll John Doe in the course
    sis_db.insert_enrollment(john_doe_id, course_id, "2024-10-06")
    print(f"Enrolled John Doe in {course['course_name']}")
# Full Implementation for Student Enrollment and Course Registration
from datetime import datetime
import sqlite3

# DatabaseManager class to handle DB connections and initializations
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

# SISDatabase class for student and course operations
class SISDatabase:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def insert_student(self, first_name, last_name, dob, email, phone):
        query = "INSERT INTO students (first_name, last_name, dob, email, phone) VALUES (?, ?, ?, ?, ?)"
        self.db_manager.cursor.execute(query, (first_name, last_name, dob, email, phone))
        self.db_manager.connection.commit()
        return self.db_manager.cursor.lastrowid  # return the ID of the newly inserted student
    
    def get_course_by_name(self, course_name):
        query = "SELECT id FROM courses WHERE course_name = ?"
        self.db_manager.cursor.execute(query, (course_name,))
        return self.db_manager.cursor.fetchone()

    def insert_course(self, course_name, course_code, teacher_id=None):
        query = "INSERT INTO courses (course_name, course_code, teacher_id) VALUES (?, ?, ?)"
        self.db_manager.cursor.execute(query, (course_name, course_code, teacher_id))
        self.db_manager.connection.commit()
        return self.db_manager.cursor.lastrowid  # return the ID of the newly inserted course

    def insert_enrollment(self, student_id, course_id, enrollment_date):
        query = "INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (?, ?, ?)"
        self.db_manager.cursor.execute(query, (student_id, course_id, enrollment_date))
        self.db_manager.connection.commit()

# Main logic for adding John Doe and enrolling in courses
if __name__ == "__main__":
    db_manager = DatabaseManager()
    sis_db = SISDatabase(db_manager)

    # Insert John Doe's information into the students table
    john_doe_id = sis_db.insert_student("John", "Doe", "1995-08-15", "john.doe@example.com", "123-456-7890")
    print(f"John Doe has been added to the system with student ID: {john_doe_id}")
    
    # Enroll John in 'Introduction to Programming' and 'Mathematics 101'
    courses = [
        {"course_name": "Introduction to Programming", "course_code": "CS101"},
        {"course_name": "Mathematics 101", "course_code": "MATH101"}
    ]

    for course in courses:
        # Check if the course already exists in the database
        course_id = sis_db.get_course_by_name(course["course_name"])
        
        # If the course doesn't exist, insert it
        if not course_id:
            course_id = sis_db.insert_course(course["course_name"], course["course_code"])
            print(f"Added course {course['course_name']} with course ID: {course_id}")
        else:
            course_id = course_id[0]  # course_id is a tuple, so we need to get the ID

        # Enroll John Doe in the course
        sis_db.insert_enrollment(john_doe_id, course_id, "2024-10-06")
        print(f"Enrolled John Doe in {course['course_name']}")

    db_manager.close()
