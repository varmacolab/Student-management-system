class Student:

  student_dictionary = {}
  school_name = "XYZ"
  def __init__(self):
    self.roll_no  = input("\n \t Enter the student Roll No:")
    self.name = input("\n \t Enter the student Name:")
    self.phone_number = input("\n \t Enter the student Phone Number:")
    self.address = input("\n \t Enter the student Address:")
    student_class = input("\n \t Enter the student Class:[Ex: 1 2 3 4 5 6 7 8 9]")
    
    if student_class in StudentClass.classes:
      StudentClass.classes[student_class].studentList.append(self)
    else:
      new_class = StudentClass(student_class)
      new_class.studentsList.append(self)
      StudentClass.classes[student_class] = new_class

    self.student_class = StudentClass.classes[student_class]

    print("\nStudent Added Successfully")

  def getStudent(self):
    print("\n --- Student Details ----\n")
    print("\t Roll No:", self.roll_no)
    print("\t Name:", self.name)
    print("\t Phone Number:", self.phone_number)
    print("\t Address:", self.address)
    print("\t Class:", self.student_class.name)

  def updateStudent(self):
    print("\t\t Select option to update student details\n")
    print("\t\t1) To Change Student name")
    print("\t\t2) To Change Student phone number")
    print("\t\t3) To Change Student address")
    print("\t\t4) To Change Student class\n")
    option = input("\t\t Enter any given above option")
    print()

    if option in ['1', '2', '3', '4']:
      if option==1:
        self.name = input('\t\t\t Enter the Student New Name')
        print('\n\t\t Student Name Updated Successfully')

      elif option==2:
        self.phone_number = input('\t\t\t Enter the Student New Phone Number')
        print('\n\t\t Student Phone Number Updated Successfully')

      elif option==3:
        self.address = input('\t\t\t Enter the Student New Address')
        print('\n\t\t Student Address Updated Successfully')

      else:
        new_class = input("\t\t\t Enter the Student New Class name")
        self.student_class.studentList.remove(self)
        try:
          self.student_class = StudentClass.classes[new_class]
          self.student_class.studentList.append(self)
        except:
          addClass = StudentClass(new_class)
          self.student_class = addClass
          addClass.studentsList.append(self)
        print("\n\t\t Student Class Updated Successfully\n")
    else:
      print('\n\t\t You have chosen wrong option')

  @classmethod
  def updateSchoolName(cls, new_school_name):
    cls.school_name = new_school_name

  @classmethod
  def getTotalStudentCount(cls):
    return len(cls.student_dictionary)

class StudentClass:
  classes={}
  def __init__(self,name):
    self.name = name
    StudentClass.classes[name] = self
    self.studentsList = []



def main():
  print("---Welcome to XYZ School ---\n")
  print("\t1) To get student details")
  print("\t2) To add new Student ")
  print("\t3) To Remove student")
  print("\t4) To Update student details")
  print("\t5) To Update School Name")
  print("\t6) To get number of students in school")
  print("\t7) To get all student details")
  print("\t8) To get any class student details")

  option = input("Enter any above given option")
  print()
  if option == "1":
    roll_no = input("\t Enter the ROll Number of a Student:")
    try:
      Student.student_dictionary[roll_no].getStudent()
    except:
      print("\t \t You have entered wrong roll number")
  elif option == "2":
    new_student = Student();
    Student.student_dictionary[new_student.roll_no] = new_student
  elif option == "3":
    roll_no = input("\t Enter the roll no of the student: ")
    try:
      student = Student.student_dictionary.pop(roll_no)
      student.student_class.studentsList.remove(student)
      print("\t\t", roll_no, 'Student Deleted Successfully')
    except:
      print("\t\t No student there to delete")
      
  elif option == "4":
    roll_no = input("\t Enter the roll no of the student: ")
    print()
    try:
      Student.student_dictionary[roll_no].updateStudent()
    except:
      print("\n\t\t You have entered wrong roll number")

      
  elif option == "5":
    new_school_name = input("\t Enter the New School Name:")
    Student.updateSchoolName(new_school_name)
    print("Schoool Name Updated Successfully")
  elif option == "6":
    print("Total number of students in school is:", Student.getTotalStudentCount())
  elif option == "7":
    if Student.student_dictionary:
      print("Total number of students in school is:", Student.getTotalStudentCount())
      print('\n Total Student List with details \n')
      for sNo, student in enumerate(Student.student_dictionary.values()):
        print("Student-", sNo+1);
        student.getStudent()
        print()
    else:
      print("No Students Available")
  elif option == "8":
    try: 
     students = StudentClass.classes[input("\tEnter the class name:")]
     print("\nStudents of Class- ", students.name)
     print(f"\nTotal numberofstudentsinclass{students.name}:{len(students.studentList)}")
     print()
     for sNo, student in enumerate(students.studentList):
      print("Student-", sNo+1);
      student.getStudent()
      print()
    except:
      print("\n\t\t You have entered wrong class name or no students there")
  
  else:
    print("Invalid option")

if __name__ == "__main__":
  option = 'y'
  while option=='y':
    main()
    option = input("\nDo you want to continue? (y/n)")
    print()

