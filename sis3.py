# Custom Exceptions

class DuplicateEnrollmentException(Exception):
    """Raised when a student is already enrolled in a course and tries to enroll again."""
    def __init__(self, message="Student is already enrolled in this course"):
        self.message = message
        super().__init__(self.message)

class CourseNotFoundException(Exception):
    """Raised when a course does not exist in the system."""
    def __init__(self, message="Course not found"):
        self.message = message
        super().__init__(self.message)

class StudentNotFoundException(Exception):
    """Raised when a student does not exist in the system."""
    def __init__(self, message="Student not found"):
        self.message = message
        super().__init__(self.message)

class TeacherNotFoundException(Exception):
    """Raised when a teacher does not exist in the system."""
    def __init__(self, message="Teacher not found"):
        self.message = message
        super().__init__(self.message)

class PaymentValidationException(Exception):
    """Raised when there is an issue with payment validation (e.g., invalid amount or date)."""
    def __init__(self, message="Payment validation failed"):
        self.message = message
        super().__init__(self.message)

class InvalidStudentDataException(Exception):
    """Raised when the student data is invalid (e.g., invalid DOB or email format)."""
    def __init__(self, message="Invalid student data provided"):
        self.message = message
        super().__init__(self.message)

class InvalidCourseDataException(Exception):
    """Raised when course data is invalid (e.g., invalid course code or instructor name)."""
    def __init__(self, message="Invalid course data provided"):
        self.message = message
        super().__init__(self.message)

class InvalidEnrollmentDataException(Exception):
    """Raised when enrollment data is invalid (e.g., missing student or course)."""
    def __init__(self, message="Invalid enrollment data provided"):
        self.message = message
        super().__init__(self.message)

class InvalidTeacherDataException(Exception):
    """Raised when teacher data is invalid (e.g., missing name or email)."""
    def __init__(self, message="Invalid teacher data provided"):
        self.message = message
        super().__init__(self.message)

class InsufficientFundsException(Exception):
    """Raised when a student attempts to enroll without enough funds."""
    def __init__(self, message="Insufficient funds for enrollment"):
        self.message = message
        super().__init__(self.message)
class SIS:
    def __init__(self):
        self.students = []
        self.courses = []
        self.teachers = []
        self.enrollments = []
        self.payments = []

    def enroll_student_in_course(self, student, course):
        # Check if student and course exist
        if student not in self.students:
            raise StudentNotFoundException(f"Student {student.first_name} {student.last_name} not found.")
        if course not in self.courses:
            raise CourseNotFoundException(f"Course {course.course_name} not found.")
        
        # Check if the student is already enrolled in the course
        for enrollment in self.enrollments:
            if enrollment.student == student and enrollment.course == course:
                raise DuplicateEnrollmentException(f"{student.first_name} is already enrolled in {course.course_name}.")
        
        # Enroll the student in the course
        enrollment = Enrollment(len(self.enrollments) + 1, student, course, "2024-10-01")
        self.enrollments.append(enrollment)
        student.enroll_in_course(course)
        course.enrollments.append(enrollment)

    def assign_teacher_to_course(self, teacher, course):
        # Check if teacher and course exist
        if teacher not in self.teachers:
            raise TeacherNotFoundException(f"Teacher {teacher.first_name} {teacher.last_name} not found.")
        if course not in self.courses:
            raise CourseNotFoundException(f"Course {course.course_name} not found.")
        
        # Assign the teacher to the course
        course.assign_teacher(teacher)
        teacher.assigned_courses.append(course)

    def record_payment(self, student, amount, payment_date):
        # Validate payment amount and date
        if amount <= 0:
            raise PaymentValidationException("Payment amount must be greater than zero.")
        if not isinstance(payment_date, str):  # Assuming we pass dates as strings for simplicity
            raise PaymentValidationException("Invalid payment date format.")

        # Check if the student exists
        if student not in self.students:
            raise StudentNotFoundException(f"Student {student.first_name} {student.last_name} not found.")

        # Record the payment
        student.make_payment(amount, payment_date)

    def generate_enrollment_report(self, course):
        # Check if the course exists
        if course not in self.courses:
            raise CourseNotFoundException(f"Course {course.course_name} not found.")

        students = [enrollment.student for enrollment in self.enrollments if enrollment.course == course]
        print(f"Enrollment Report for {course.course_name}: {[student.first_name for student in students]}")

    def generate_payment_report(self, student):
        # Check if the student exists
        if student not in self.students:
            raise StudentNotFoundException(f"Student {student.first_name} {student.last_name} not found.")

        print(f"Payment Report for {student.first_name} {student.last_name}: {student.get_payment_history()}")

    def calculate_course_statistics(self, course):
        # Check if the course exists
        if course not in self.courses:
            raise CourseNotFoundException(f"Course {course.course_name} not found.")

        num_enrollments = len(course.get_enrollments())
        total_payments = sum(payment.amount for payment in self.payments if payment.student_id in course.get_enrollments())
        print(f"Course: {course.course_name}")
        print(f"Number of Enrollments: {num_enrollments}")
        print(f"Total Payments: {total_payments}")
