class Person:
    "부모 클래스"

    def __init__(self, name, phoneNumber):
        self.Name = name
        self.PhoneNumber = phoneNumber

    def PrintInfo(self):
        print("Info(Name:{0}, phone Number,: {1})" .format(self.Name, self.PhoneNumber))

    def PrintPersonData(self):
        print("Person(Name:{0}, phone Number: {1}" .format(self.Name, self.PhoneNumber))

class Student(Person):
    "자식 클래스"

    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber)        
        self.Subject = subject
        self.StudentID = studentID

    def PrintStudentData(self):
        print("Student(Subject:{0}, Student ID:{1})".format(self.Subject, self.StudentID))

p = Person("Derick", "010-123-4567")
s = Student("Marry", "011", "computer","123")

s.PrintStudentData()
dir(s)
p.__dict__ 
s.__dict__

issubclass(Student, Person)
