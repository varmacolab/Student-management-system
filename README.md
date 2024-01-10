# XYZ School Management System - Object-Oriented Programming (OOP) Documentation

The XYZ School Management System is designed using Object-Oriented Programming (OOP) principles, providing a structured and modular approach to managing student details, classes, and school-related information.

## Classes

### 1. Student Class

The `Student` class manages individual student details and encapsulates properties and behaviors related to a student.

#### Attributes:

- **roll_no:** Represents the unique roll number of each student.
- **name:** Stores the name of the student.
- **phone_number:** Holds the contact number of the student.
- **address:** Stores the address of the student.
- **student_class:** Represents the class to which the student belongs.

#### Methods:

- **`__init__(self):`** Constructor method to initialize a new student object. It prompts the user to input student details and assigns the student to the respective class.

- **`getStudent(self):`** Displays the details of a student.

- **`updateStudent(self):`** Allows updating student information, including name, phone number, address, and class.

- **`@classmethod updateSchoolName(cls, new_school_name):`** Class method to update the school name.

- **`@classmethod getTotalStudentCount(cls):`** Class method to retrieve the total number of students in the school.

### 2. StudentClass Class

The `StudentClass` class manages classes in the school and encapsulates properties and behaviors related to a class.

#### Attributes:

- **name:** Represents the name of the class.
- **studentsList:** Holds a list of students belonging to the class.

#### Methods:

- **`__init__(self, name):`** Constructor method to initialize a new class object.

## Main Function

The `main()` function serves as the program's entry point and orchestrates the interaction with the system. It provides a menu-driven interface for users to perform various tasks.

### Design Considerations

1. **Encapsulation:** Each class encapsulates related attributes and methods, promoting modular and organized code.

2. **Inheritance:** While not explicitly used, the design focuses on composition and encapsulation. Inheritance could be incorporated for creating specific types of students.

3. **Polymorphism:** Achieved through method overloading within the `Student` class, where the `updateStudent` method handles different types of updates based on user input.

4. **Composition:** The `Student` class contains an instance of the `StudentClass` class to manage the association between students and their classes.

## Usage

1. Create instances of the `Student` and `StudentClass` classes to represent students and classes in the school.
2. Interact with the system using the `main()` function, selecting options to perform various tasks.
3. Leverage OOP principles for code organization, encapsulation, and modular design.

This XYZ School Management System exemplifies the effective application of OOP principles, providing a structured and maintainable solution for school management.
