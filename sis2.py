class Student:
    def __init__(self, student_id, first_name, last_name, dob, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone_number = phone_number
        self.courses = []  # List to track enrolled courses
        self.payments = []  # List to track payments made by the student

    def enroll_in_course(self, course):
        self.courses.append(course)
        print(f"Student {self.first_name} {self.last_name} enrolled in {course.course_name}")

    def update_student_info(self, first_name, last_name, dob, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone_number = phone_number
        print(f"Student {self.student_id} information updated.")

    def make_payment(self, amount, payment_date):
        payment = Payment(self.student_id, amount, payment_date)
        self.payments.append(payment)
        print(f"Payment of {amount} made by {self.first_name} {self.last_name} on {payment_date}.")

    def display_student_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"DOB: {self.dob}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone_number}")

    def get_enrolled_courses(self):
        return [course.course_name for course in self.courses]

    def get_payment_history(self):
        return [(payment.amount, payment.payment_date) for payment in self.payments]
class Course:
    def __init__(self, course_id, course_name, course_code, instructor_name):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.teacher = None
        self.enrollments = []

    def assign_teacher(self, teacher):
        self.teacher = teacher
        print(f"Teacher {teacher.first_name} {teacher.last_name} assigned to {self.course_name}.")

    def update_course_info(self, course_code, course_name, instructor_name):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor_name = instructor_name
        print(f"Course {self.course_id} information updated.")

    def display_course_info(self):
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Instructor: {self.instructor_name}")

    def get_enrollments(self):
        return [enrollment.student_id for enrollment in self.enrollments]

    def get_teacher(self):
        return self.teacher
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
class Teacher:
    def __init__(self, teacher_id, first_name, last_name, email):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.assigned_courses = []

    def update_teacher_info(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        print(f"Teacher {self.teacher_id} information updated.")

    def display_teacher_info(self):
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")

    def get_assigned_courses(self):
        return [course.course_name for course in self.assigned_courses]
class Payment:
    def __init__(self, student_id, amount, payment_date):
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date

    def get_student(self):
        return self.student_id

    def get_payment_amount(self):
        return self.amount

    def get_payment_date(self):
        return self.payment_date
class Sis:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []
        self.enrollments = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def add_enrollment(self, student, course, date):
        for enrollment in self.enrollments:
            if enrollment['student'] == student and enrollment['course'] == course:
                raise DuplicateEnrollmentException("Student is already enrolled in this course.")
        self.enrollments.append({"student": student, "course": course, "date": date})

    def add_payment(self, student, amount, date):
        # Payment processing logic here
        print(f"Payment of {amount} added for {student.first_name} on {date}")

    def get_enrollments_for_student(self, student):
        return [enrollment['course'] for enrollment in self.enrollments if enrollment['student'] == student]

    def get_courses_for_teacher(self, teacher):
        return [course for course in self.courses if course.teacher == teacher]

    def assign_course_to_teacher(self, course, teacher):
        course.teacher = teacher

    def generate_enrollment_report(self, course_name):
        report = []
        for enrollment in self.enrollments:
            if enrollment['course'].name == course_name:
                student = enrollment['student']
                report.append((student.first_name, student.last_name))
        return report

class DuplicateEnrollmentException(Exception):
    pass
