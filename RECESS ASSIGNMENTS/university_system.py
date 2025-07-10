# Base class representing a person at the university
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display_info(self):
        # Method to display basic personal details
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")


# Subclass for students, inheriting from Person
class Student(Person):
    def __init__(self, first_name, last_name, age, reg_number, course):
        super().__init__(first_name, last_name, age)  # call base constructor
        self.reg_number = reg_number
        self.course = course

    def display_info(self):
        super().display_info()  # reuse the Person display
        print(f"Registration Number: {self.reg_number}")
        print(f"Course Enrolled: {self.course}")
        print("_____________________________________")


# Subclass for lecturers, inheriting from Person
class Lecturer(Person):
    def __init__(self, first_name, last_name, age, lecturer_id, title):
        super().__init__(first_name, last_name, age)
        self.lecturer_id = lecturer_id
        self.title = title

    def display_info(self):
        super().display_info()
        print(f"Lecturer ID: {self.lecturer_id}")
        print(f"Academic Title: {self.title}")
        print("_____________________________________")


# Subclass for non-teaching staff
class Staff(Person):
    def __init__(self, first_name, last_name, age, staff_id, role):
        super().__init__(first_name, last_name, age)
        self.staff_id = staff_id
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Role: {self.role}")
        print("_____________________________________")


# Instantiate sample objects
student = Student("Brenda", "Katusiime", 21, "22/U/15489", "BSc. Computer Science")
lecturer = Lecturer("Dr. Peter", "Okello", 45, "L-102", "Senior Lecturer")
staff = Staff("Angela", "Nakato", 38, "STF-345", "Admissions Officer")

# Display each person’s info
student.display_info()
lecturer.display_info()
staff.display_info()

# Demonstrating Polymorphism
print("======= Displaying All People Using Polymorphism =======")
people = [student, lecturer, staff]
for person in people:
    person.display_info()  

