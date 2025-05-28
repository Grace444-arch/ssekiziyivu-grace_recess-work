class Person:
    def __init__(self, name, age, person_id):
        self.name = name
        self.age = age
        self.person_id = person_id
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.person_id}")

class Student(Person):
    def __init__(self, name, age, person_id, course, year):
        super().__init__(name, age, person_id)
        self.course = course
        self.year = year
        self.enrolled_courses = []
        self.grades = {}

    def display_info(self):
        super().display_info()
        print(f"Course: {self.course}")
        print(f"Year: {self.year}")
        print("Enrolled Courses:", ", ".join(self.enrolled_courses) if self.enrolled_courses else "None")

    def enroll_course(self, course_name):
        if course_name not in self.enrolled_courses:
            self.enrolled_courses.append(course_name)
            print(f"Successfully enrolled in {course_name}.")
        else:
            print(f"Already enrolled in {course_name}.")
    
    def view_grades(self):
        if self.grades:
            print("\n--- Your Grades ---")
            for course, grade in self.grades.items():
                print(f"{course}: {grade}")
        else:
            print("No grades available yet")

class Lecturer(Person):
    def __init__(self, name, age, person_id, department, courses_taught):
        super().__init__(name, age, person_id)
        self.department = department
        self.courses_taught = courses_taught

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print("Courses Taught:", ", ".join(self.courses_taught))

    def assign_grade(self, student, course, grade):
        if course in self.courses_taught:
            if course in student.enrolled_courses:
                student.grades[course] = grade
                print(f"Grade {grade} assigned to {student.name} for {course}.")
            else:
                print(f"{student.name} is not enrolled in {course}.")
        else:
            print(f"You don't teach {course}.")

class Staff(Person):
    def __init__(self, name, age, person_id, role):
        super().__init__(name, age, person_id)
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")

class UniversitySystem:
    def __init__(self):
        self.students = []
        self.lecturers = []
        self.staff = []
        self.available_courses = ["cybersecurity", "software engineering", "data science", "networking"]

    def register_student(self):
        print("\n---Student Registration---") 
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        person_id = input("Enter student ID: ")
        course = input("Enter course: ")
        year = input("Enter year of study: ")
        student = Student(name, age, person_id, course, year)
        self.students.append(student)
        print(f"Student {name} registered successfully.")
        return student
    
    def register_lecturer(self):
        print("\n---Lecturer Registration---")
        name = input("Enter lecturer name: ")
        age = int(input("Enter lecturer age: "))
        person_id = input("Enter lecturer ID: ")
        department = input("Enter department: ")
        
        print("Available courses:", ", ".join(self.available_courses))
        courses_input = input("Enter courses taught (comma-separated): ")
        courses_taught = [course.strip() for course in courses_input.split(",")]
        
        lecturer = Lecturer(name, age, person_id, department, courses_taught)
        self.lecturers.append(lecturer)
        print(f"Lecturer {name} registered successfully.")
        return lecturer
    
    def register_staff(self):
        print("\n---Staff Registration---")
        name = input("Enter staff name: ")
        age = int(input("Enter staff age: "))
        person_id = input("Enter staff ID: ")
        role = input("Enter role: ")
        
        staff = Staff(name, age, person_id, role)
        self.staff.append(staff)
        print(f"Staff {name} registered successfully.")
        return staff
    
    def student_menu(self, student):
        while True:
            print("\n---Student Menu---")
            print("1. View Info")
            print("2. Enroll in Course")
            print("3. View Grades")
            print("4. View Available Courses")
            print("5. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                print("\n---Student Info---")
                student.display_info()
            elif choice == "2":
                print("\nAvailable Courses:", ", ".join(self.available_courses))
                course_name = input("Enter course name to enroll: ")
                if course_name in self.available_courses:
                    student.enroll_course(course_name)
                else:
                    print("Course not available!")
            elif choice == "3":
                student.view_grades()
            elif choice == "4":
                print("\nAvailable Courses:", ", ".join(self.available_courses))
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def lecturer_menu(self, lecturer):
        while True:
            print(f"\n--- Welcome {lecturer.name} (Lecturer) ---")
            print("1. View Profile")
            print("2. Assign Grade to Student")
            print("3. View All Students")
            print("4. Back to Main Menu")
            
            choice = input("Choose option: ")
            
            if choice == "1":
                print("\n--- Your Profile ---")
                lecturer.display_info()
            elif choice == "2":
                if not self.students:
                    print("No students registered yet!")
                    continue
                
                # Show only students enrolled in lecturer's courses
                eligible_students = []
                for student in self.students:
                    for course in lecturer.courses_taught:
                        if course in student.enrolled_courses:
                            eligible_students.append((student, course))
                            break
                
                if not eligible_students:
                    print("No students are enrolled in your courses yet!")
                    continue
                
                print("\nStudents enrolled in your courses:")
                for i, (student, _) in enumerate(eligible_students):
                    enrolled_in_your_courses = [c for c in student.enrolled_courses if c in lecturer.courses_taught]
                    print(f"{i+1}. {student.name} (ID: {student.person_id}) - Enrolled in: {', '.join(enrolled_in_your_courses)}")
                
                try:
                    student_idx = int(input("Select student number: ")) - 1
                    selected_student = eligible_students[student_idx][0]
                    
                    # Show only courses this student is enrolled in that the lecturer teaches
                    student_courses = [c for c in selected_student.enrolled_courses if c in lecturer.courses_taught]
                    print(f"\nCourses you can grade for {selected_student.name}: {', '.join(student_courses)}")
                    course = input("Enter course to grade: ")
                    
                    if course in student_courses:
                        grade = input("Enter grade: ")
                        lecturer.assign_grade(selected_student, course, grade)
                    else:
                        print("Invalid course selection!")
                        
                except (ValueError, IndexError):
                    print("Invalid selection!")
            elif choice == "3":
                if self.students:
                    print("\n--- All Students ---")
                    for student in self.students:
                        print("-" * 30)
                        student.display_info()
                else:
                    print("No students registered yet!")
            elif choice == "4":
                break
    
    def staff_menu(self, staff):
        while True:
            print(f"\n--- Welcome {staff.name} (Staff) ---")
            print("1. View Profile")
            print("2. View All University Members")
            print("3. Back to Main Menu")
            
            choice = input("Choose option: ")
            
            if choice == "1":
                print("\n--- Your Profile ---")
                staff.display_info()
            elif choice == "2":
                print("\n--- University Members ---")
                print(f"\nStudents ({len(self.students)}):")
                for s in self.students:
                    print(f"- {s.name} ({s.course})")
                
                print(f"\nLecturers ({len(self.lecturers)}):")
                for l in self.lecturers:
                    print(f"- {l.name} ({l.department})")
                
                print(f"\nStaff ({len(self.staff)}):")
                for st in self.staff:
                    print(f"- {st.name} ({st.role})")
            elif choice == "3":
                break
    
    def login(self):
        person_id = input("Enter your ID: ")
        
        # Check students
        for student in self.students:
            if student.person_id == person_id:
                return student, "student"
        
        # Check lecturers
        for lecturer in self.lecturers:
            if lecturer.person_id == person_id:
                return lecturer, "lecturer"
        
        # Check staff
        for staff in self.staff:
            if staff.person_id == person_id:
                return staff, "staff"
        
        return None, None
    
    def run(self):
        print("=== UNIVERSITY MANAGEMENT SYSTEM ===")
        
        while True:
            print("\n--- Main Menu ---")
            print("1. Register as Student")
            print("2. Register as Lecturer")
            print("3. Register as Staff")
            print("4. Login")
            print("5. Exit")
            
            choice = input("Choose option: ")
            
            if choice == "1":
                self.register_student()
            elif choice == "2":
                self.register_lecturer()
            elif choice == "3":
                self.register_staff()
            elif choice == "4":
                person, role = self.login()
                if person:
                    if role == "student":
                        self.student_menu(person)
                    elif role == "lecturer":
                        self.lecturer_menu(person)
                    elif role == "staff":
                        self.staff_menu(person)
                else:
                    print("Invalid ID! Please register first.")
            elif choice == "5":
                print("Thank you for using the University Management System!")
                break
            else:
                print("Invalid choice!")

# Run the system
if __name__ == "__main__":
    university = UniversitySystem()
    university.run()