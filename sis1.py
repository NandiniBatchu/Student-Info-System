from datetime import datetime

# Student Class
class Student:
    def __init__(self, student_id, first_name, last_name, dob, email, phone):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone = phone
        self.courses = []
        self.payments = []
    
    def enroll_in_course(self, course):
        self.courses.append(course)
    
    def update_student_info(self, first_name, last_name, dob, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone = phone
    
    def make_payment(self, amount, payment_date):
        payment = Payment(len(self.payments) + 1, self.student_id, amount, payment_date)
        self.payments.append(payment)
    
    def display_student_info(self):
        print(f"ID: {self.student_id}, Name: {self.first_name} {self.last_name}, DOB: {self.dob}, Email: {self.email}, Phone: {self.phone}")
    
    def get_enrolled_courses(self):
        return self.courses
    
    def get_payment_history(self):
        return self.payments

# Course Class
class Course:
    def __init__(self, course_id, course_name, course_code, instructor_name):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.enrollments = []
    
    def assign_teacher(self, teacher):
        self.instructor_name = teacher.first_name + " " + teacher.last_name
    
    def update_course_info(self, course_code, course_name, instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor_name = instructor
    
    def display_course_info(self):
        print(f"ID: {self.course_id}, Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor_name}")
    
    def get_enrollments(self):
        return self.enrollments

# Enrollment Class
class Enrollment:
    def __init__(self, enrollment_id, student, course, enrollment_date):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date
    
    def get_student(self):
        return self.student
    
    def get_course(self):
        return self.course

# Teacher Class
class Teacher:
    def __init__(self, teacher_id, first_name, last_name, email):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.courses = []
    
    def update_teacher_info(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    def display_teacher_info(self):
        print(f"ID: {self.teacher_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}")
    
    def get_assigned_courses(self):
        return self.courses

# Payment Class
class Payment:
    def __init__(self, payment_id, student_id, amount, payment_date):
        self.payment_id = payment_id
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date
    
    def get_student(self):
        return self.student_id
    
    def get_payment_amount(self):
        return self.amount
    
    def get_payment_date(self):
        return self.payment_date

# SIS Class
class SIS:
    def __init__(self):
        self.students = []
        self.courses = []
        self.teachers = []
        self.enrollments = []
        self.payments = []

    def add_enrollment(self, student, course, enrollment_date):
        enrollment = Enrollment(len(self.enrollments) + 1, student, course, enrollment_date)
        student.enroll_in_course(course)
        course.enrollments.append(student)
        self.enrollments.append(enrollment)
    
    def assign_course_to_teacher(self, course, teacher):
        course.assign_teacher(teacher)
        teacher.courses.append(course)
    
    def add_payment(self, student, amount, payment_date):
        student.make_payment(amount, payment_date)
        payment = Payment(len(self.payments) + 1, student.student_id, amount, payment_date)
        self.payments.append(payment)

    def get_enrollments_for_student(self, student):
        return [course.course_name for course in student.get_enrolled_courses()]

    def get_courses_for_teacher(self, teacher):
        return [course.course_name for course in teacher.get_assigned_courses()]
    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.first_name} {student.last_name} added.")


def main():
    # Create SIS instance
    sis = SIS()

    # Create students
    student1 = Student(1, "Alice", "Doe", "2000-01-01", "alice@example.com", "1234567890")
    student2 = Student(2, "Bob", "Smith", "1999-06-15", "bob@example.com", "0987654321")
    
    # Create teacher
    teacher1 = Teacher(1, "John", "Williams", "john@example.com")
    teacher2 = Teacher(2, "Johnson", "Wallet", "johnson@example.com")
    
    # Create course
    course1 = Course(1, "Mathematics", "MATH101", teacher1.first_name + " " + teacher1.last_name)
    course2 = Course(2, "Physics", "PHYSICS102", teacher2.first_name + " " + teacher2.last_name)

    
    # Add students, teachers, and courses to SIS
    sis.students.extend([student1, student2])
    sis.teachers.extend([teacher1, teacher2])
    sis.teachers.append(teacher1)
    sis.courses.append(course1)
    sis.courses.append(course2)
    sis.teachers.append(teacher2)

    
    # Enroll student in course
    sis.add_enrollment(student1, course1, "2024-10-06")
    sis.add_enrollment(student2, course2, "2024-09-06")

    # Assign teacher to course
    sis.assign_course_to_teacher(course1, teacher1)
    sis.assign_course_to_teacher(course2, teacher2)

    # Record a payment for the student
    sis.add_payment(student1, 500, "2024-10-06")
    sis.add_payment(student2, 600, "2024-09-06")

    # Retrieve enrollments for student
    student_courses = sis.get_enrollments_for_student(student1)
    print(f"{student1.first_name} is enrolled in the following courses: {student_courses}")
    print(f"{student2.first_name} is enrolled in the following courses: {student_courses}")
    student_courses = sis.get_enrollments_for_student(student2)
    print(f"{student2.first_name} is enrolled in the following courses: {student_courses}")
    print(f"{student2.first_name} is enrolled in the following courses: {student_courses}")


    # Retrieve courses for teacher
    teacher_courses = sis.get_courses_for_teacher(teacher1)
    print(f"{teacher1.first_name} is teaching the following courses: {teacher_courses}")
    print(f"{teacher2.first_name} is teaching the following courses: {teacher_courses}")
    teacher_courses = sis.get_courses_for_teacher(teacher2)
    print(f"{teacher1.first_name} is teaching the following courses: {teacher_courses}")
    print(f"{teacher2.first_name} is teaching the following courses: {teacher_courses}")


if __name__ == "__main__":
    main()
