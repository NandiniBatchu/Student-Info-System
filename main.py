
def main():
    # Create SIS instance
    sis = SIS()  # Fix the case here

    # Create students
    student1 = Student(1, "Alice", "Doe", "2000-01-01", "alice@example.com", "1234567890")
    student2 = Student(2, "Bob", "Smith", "1999-06-15", "bob@example.com", "0987654321")
    
    # Create teacher
    teacher1 = Teacher(1, "John", "Williams", "john@example.com")
    
    # Create course
    course1 = Course(1, "Mathematics", "MATH101", teacher1)
    
    # Add students, teachers, and courses to SIS
    sis.students.extend([student1, student2])
    sis.teachers.append(teacher1)
    sis.courses.append(course1)
    
    # Enroll student in course
    try:
        sis.add_enrollment(student1, course1, "2024-10-06")
    except DuplicateEnrollmentException as e:
        print(e)

    # Assign teacher to course
    try:
        sis.assign_course_to_teacher(course1, teacher1)
    except Exception as e:
        print(e)

    # Record a payment for the student
    sis.add_payment(student1, 500, "2024-10-06")

    # Retrieve enrollments for student
    student_courses = sis.get_enrollments_for_student(student1)
    print(f"{student1.first_name} is enrolled in the following courses: {student_courses}")

    # Retrieve courses for teacher
    teacher_courses = sis.get_courses_for_teacher(teacher1)
    print(f"{teacher1.first_name} is teaching the following courses: {teacher_courses}")

    # TASK 8 - Enroll new student John Doe in courses
    john_doe = Student(3, "John", "Doe", "1995-08-15", "john.doe@example.com", "123-456-7890")
    sis.add_student(john_doe)

    # Add courses for John Doe
    course_programming = Course(3, "Introduction to Programming", "CS101","Bhavana")
    course_math = Course(4, "Mathematics 101", "MATH101","keerthi")
    sis.add_course(course_programming)
    sis.add_course(course_math)

    sis.add_enrollment(john_doe, course_programming, "2024-10-06")
    sis.add_enrollment(john_doe, course_math, "2024-10-06")

    # TASK 9 - Assign new teacher Sarah Smith to Advanced Database Management
    sarah_smith = Teacher(2, "Sarah", "Smith", "sarah.smith@example.com", "Computer Science")
    sis.add_teacher(sarah_smith)

    course_db_management = Course(6, "Advanced Database Management", "CS302")
    sis.add_course(course_db_management)
    sis.assign_course_to_teacher(course_db_management, sarah_smith)

    # TASK 10 - Record payment for student Jane Johnson
    jane_johnson = Student(101, "Jane", "Johnson", "2000-05-01", "jane.johnson@example.com", "555-555-5555")
    sis.add_student(jane_johnson)
    sis.add_payment(jane_johnson, 500, "2023-04-10")

    # TASK 11 - Generate Enrollment Report for Computer Science 101
    course_cs101 = Course(5, "Computer Science 101", "CS101")
    sis.add_course(course_cs101)
    sis.add_enrollment(john_doe, course_cs101, "2024-10-06")
    print(f"Enrolled {john_doe.first_name} {john_doe.last_name} in Computer Science 101")

    report = sis.generate_enrollment_report("Computer Science 101")
    print("Enrollment Report for Computer Science 101:")
    for student in report:
        print(f"Student: {student[0]} {student[1]}")

if __name__ == "__main__":
    main()
