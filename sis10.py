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

    # Retrieve a course by name
    def get_course_by_name(self, course_name):
        query = "SELECT * FROM courses WHERE course_name = ?"
        self.db_manager.cursor.execute(query, (course_name,))
        return self.db_manager.cursor.fetchone()

    # Retrieve enrollment records for a specific course
    def get_enrollments_for_course(self, course_id):
        query = '''SELECT students.first_name, students.last_name, enrollments.enrollment_date 
                   FROM enrollments 
                   JOIN students ON enrollments.student_id = students.id 
                   WHERE enrollments.course_id = ?'''
        self.db_manager.cursor.execute(query, (course_id,))
        return self.db_manager.cursor.fetchall()

    # Generate enrollment report for a course
    def generate_enrollment_report(self, course_name):
        course = self.get_course_by_name(course_name)
        if not course:
            return f"Course '{course_name}' not found."
        
        course_id = course[0]  # assuming the first column is the ID
        enrollments = self.get_enrollments_for_course(course_id)

        if not enrollments:
            return f"No students enrolled in '{course_name}'."

        report_lines = [f"Enrollment Report for {course_name}:"]
        report_lines.append(f"{'Student Name':<30}{'Enrollment Date':<15}")
        report_lines.append("=" * 45)

        for first_name, last_name, enrollment_date in enrollments:
            report_lines.append(f"{first_name + ' ' + last_name:<30}{enrollment_date:<15}")

        return "\n".join(report_lines)

# Main logic for generating enrollment report
if __name__ == "__main__":
    db_manager = DatabaseManager()
    sis_db = SISDatabase(db_manager)

    # Generate report for "Computer Science 101"
    course_name = "Computer Science 101"
    report = sis_db.generate_enrollment_report(course_name)

    # Print or save the report
    print(report)

    db_manager.close()

# Save report to a text file ( optional )
with open("enrollment_report.txt", "w") as file:
    file.write(report)
print("Report saved to enrollment_report.txt")
