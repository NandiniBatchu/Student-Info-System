class SISDatabase:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    # Insert a new teacher
    def insert_teacher(self, first_name, last_name, email, expertise):
        query = "INSERT INTO teachers (first_name, last_name, email, expertise) VALUES (?, ?, ?, ?)"
        self.db_manager.cursor.execute(query, (first_name, last_name, email, expertise))
        self.db_manager.connection.commit()
        return self.db_manager.cursor.lastrowid  # return the ID of the newly inserted teacher

    # Retrieve a course by its course code
    def get_course_by_code(self, course_code):
        query = "SELECT * FROM courses WHERE course_code = ?"
        self.db_manager.cursor.execute(query, (course_code,))
        return self.db_manager.cursor.fetchone()

    # Update course with the assigned teacher
    def assign_teacher_to_course(self, course_id, teacher_id):
        query = "UPDATE courses SET teacher_id = ? WHERE id = ?"
        self.db_manager.cursor.execute(query, (teacher_id, course_id))
        self.db_manager.connection.commit()
# Insert Sarah Smith into the teachers table
sarah_smith_id = sis_db.insert_teacher("Sarah", "Smith", "sarah.smith@example.com", "Computer Science")
print(f"Sarah Smith has been added to the system with teacher ID: {sarah_smith_id}")
# Retrieve the course "Advanced Database Management" by its course code
course = sis_db.get_course_by_code("CS302")

if course:
    course_id = course[0]  # The first column is the course ID
    # Assign Sarah Smith to the course
    sis_db.assign_teacher_to_course(course_id, sarah_smith_id)
    print(f"Sarah Smith has been assigned to teach {course[1]} (Course ID: {course_id})")
else:
    print("Course 'Advanced Database Management' not found in the system.")
# Full Implementation for Teacher Assignment to a Course
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

    # Insert a new teacher
    def insert_teacher(self, first_name, last_name, email, expertise):
        query = "INSERT INTO teachers (first_name, last_name, email, expertise) VALUES (?, ?, ?, ?)"
        self.db_manager.cursor.execute(query, (first_name, last_name, email, expertise))
        self.db_manager.connection.commit()
        return self.db_manager.cursor.lastrowid  # return the ID of the newly inserted teacher

    # Retrieve a course by its course code
    def get_course_by_code(self, course_code):
        query = "SELECT * FROM courses WHERE course_code = ?"
        self.db_manager.cursor.execute(query, (course_code,))
        return self.db_manager.cursor.fetchone()

    # Update course with the assigned teacher
    def assign_teacher_to_course(self, course_id, teacher_id):
        query = "UPDATE courses SET teacher_id = ? WHERE id = ?"
        self.db_manager.cursor.execute(query, (teacher_id, course_id))
        self.db_manager.connection.commit()

# Main logic for assigning Sarah Smith to teach Advanced Database Management
if __name__ == "__main__":
    db_manager = DatabaseManager()
    sis_db = SISDatabase(db_manager)

    # Insert Sarah Smith into the teachers table
    sarah_smith_id = sis_db.insert_teacher("Sarah", "Smith", "sarah.smith@example.com", "Computer Science")
    print(f"Sarah Smith has been added to the system with teacher ID: {sarah_smith_id}")

    # Retrieve the course "Advanced Database Management" by its course code
    course = sis_db.get_course_by_code("CS302")

    if course:
        course_id = course[0]  # The first column is the course ID
        # Assign Sarah Smith to the course
        sis_db.assign_teacher_to_course(course_id, sarah_smith_id)
        print(f"Sarah Smith has been assigned to teach {course[1]} (Course ID: {course_id})")
    else:
        print("Course 'Advanced Database Management' not found in the system.")

    db_manager.close()
