class Student:
    def __init__(self, student_id, first_name, last_name, dob, email, phone):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone = phone
        # List to store enrollments
        self.enrollments = []
        # List to store payments
        self.payments = []

    def enroll_in_course(self, course):
        self.enrollments.append(course)

    def make_payment(self, amount, payment_date):
        payment = Payment(len(self.payments) + 1, self, amount, payment_date)
        self.payments.append(payment)

    def get_enrolled_courses(self):
        return [enrollment.course_name for enrollment in self.enrollments]

    def get_payment_history(self):
        return [(payment.amount, payment.payment_date) for payment in self.payments]

    def display_student_info(self):
        print(f"Student ID: {self.student_id}, Name: {self.first_name} {self.last_name}")
class Course:
    def __init__(self, course_id, course_name, course_code, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        # List to store enrollments
        self.enrollments = []
        # Property to store assigned teacher
        self.teacher = instructor

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def get_enrollments(self):
        return self.enrollments

    def display_course_info(self):
        print(f"Course ID: {self.course_id}, Course Name: {self.course_name}, Instructor: {self.teacher.first_name} {self.teacher.last_name}")
class Enrollment:
    def __init__(self, enrollment_id, student, course, enrollment_date):
        self.enrollment_id = enrollment_id
        # Reference to a student object
        self.student = student
        # Reference to a course object
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
        # List to store assigned courses
        self.assigned_courses = []

    def update_teacher_info(self, name, email):
        self.first_name, self.last_name = name.split()
        self.email = email

    def get_assigned_courses(self):
        return self.assigned_courses

    def display_teacher_info(self):
        print(f"Teacher ID: {self.teacher_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}")
class Payment:
    def __init__(self, payment_id, student, amount, payment_date):
        self.payment_id = payment_id
        # Reference to the student who made the payment
        self.student = student
        self.amount = amount
        self.payment_date = payment_date

    def get_student(self):
        return self.student

    def get_payment_amount(self):
        return self.amount

    def get_payment_date(self):
        return self.payment_date
class SIS:
    def __init__(self):
        self.students = []
        self.courses = []
        self.teachers = []
        self.enrollments = []
        self.payments = []

    def enroll_student_in_course(self, student, course):
        enrollment = Enrollment(len(self.enrollments) + 1, student, course, "2024-10-01")
        self.enrollments.append(enrollment)
        student.enroll_in_course(course)
        course.enrollments.append(enrollment)

    def assign_teacher_to_course(self, teacher, course):
        course.assign_teacher(teacher)
        teacher.assigned_courses.append(course)

    def record_payment(self, student, amount, payment_date):
        payment = Payment(len(self.payments) + 1, student, amount, payment_date)
        self.payments.append(payment)
        student.payments.append(payment)
