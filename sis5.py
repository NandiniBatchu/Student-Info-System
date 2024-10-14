from datetime import datetime

# SIS Class: Handles relationships and interactions
class SIS:
    def __init__(self):
        self.students = []
        self.courses = []
        self.teachers = []
        self.enrollments = []
        self.payments = []

    def add_enrollment(self, student, course, enrollment_date):
        # Check if the student is already enrolled in the course
        for enrollment in self.enrollments:
            if enrollment.student == student and enrollment.course == course:
                raise Exception(f"{student.first_name} is already enrolled in {course.course_name}")
        
        # Create a new enrollment and add it to both student and course
        enrollment = Enrollment(len(self.enrollments) + 1, student, course, enrollment_date)
        student.enroll_in_course(course)
        course.enrollments.append(student)
        self.enrollments.append(enrollment)
    
    def assign_course_to_teacher(self, course, teacher):
        # Assign course to the teacher and update teacher's list of assigned courses
        course.assign_teacher(teacher)
        teacher.courses.append(course)
    
    def add_payment(self, student, amount, payment_date):
        # Add a payment to the student's payment history
        student.make_payment(amount, payment_date)
        payment = Payment(len(self.payments) + 1, student.student_id, amount, payment_date)
        self.payments.append(payment)

    def get_enrollments_for_student(self, student):
        # Return a list of course names the student is enrolled in
        return [course.course_name for course in student.get_enrolled_courses()]

    def get_courses_for_teacher(self, teacher):
        # Return a list of course names the teacher is teaching
        return [course.course_name for course in teacher.get_assigned_courses()]

def main():
    # Create SIS instance
    sis = SIS()

    # Create students
    student1 = Student(1, "Alice", "Doe", "2000-01-01", "alice@example.com", "1234567890")
    student2 = Student(2, "Bob", "Smith", "1999-06-15", "bob@example.com", "0987654321")
    
    # Create teacher
    teacher1 = Teacher(1, "John", "Williams", "john@example.com")
    
    # Create course
    course1 = Course(1, "Mathematics", "MATH101", teacher1.first_name + " " + teacher1.last_name)
    course2 = Course(2, "Science", "SCI101", "TBD")
    
    # Add students, teachers, and courses to SIS
    sis.students.extend([student1, student2])
    sis.teachers.append(teacher1)
    sis.courses.extend([course1, course2])
    
    # Enroll student in course
    try:
        sis.add_enrollment(student1, course1, "2024-10-06")
        sis.add_enrollment(student2, course2, "2024-10-06")
    except Exception as e:
        print(e)

    # Assign teacher to course
    try:
        sis.assign_course_to_teacher(course1, teacher1)
    except Exception as e:
        print(e)

    # Record a payment for the student
    sis.add_payment(student1, 500, "2024-10-06")

    # Retrieve enrollments for student
    student1_courses = sis.get_enrollments_for_student(student1)
    print(f"{student1.first_name} is enrolled in the following courses: {', '.join(student1_courses)}")

    # Retrieve courses for teacher
    teacher_courses = sis.get_courses_for_teacher(teacher1)
    print(f"{teacher1.first_name} is teaching the following courses: {', '.join(teacher_courses)}")

if __name__ == "__main__":
    main()
