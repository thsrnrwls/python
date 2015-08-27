class Person:
    "부모 클래스"

    def __init__(self, name, phoneNumber):
        self.Name = name
        self.PhoneNumber = phoneNumber

    def PrintInfo(self):
        print("Info(Name:{0}, phone Number,: {1})" .format(self.Name, self.PhoneNumber))

    def PrintPersonData(self):
        print("Person(Name:{0}, phone Number: {1}" .format(self.Name, self.PhoneNumber))

class Student:
    "자식 클래스"

    def __init__(self, name, phoneNumber, subject, studentID):
        self.Name = name
        self.PhoneNumber = phoneNumber
        self.Subject = subject
        self.StudentID = studentID

p = Person("Derick", "010-123-4567")
s = Student("Marry", "011", "computer","123")

p.__dict__ 
s.__dict__

issubclass(Student, Person)
