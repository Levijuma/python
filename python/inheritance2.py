class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def print_name(self):
        print(f"My name is {self.first_name} {self.last_name} ad i'm {self.age} years old")

class Student(Person):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)


myStudent=Student(first_name='Fortune',last_name='Ushindi',age='19')
myStudent.print_name()
myStudent2=Student(first_name='Angela',last_name='John',age='19')
myStudent2.print_name()
myStudent3=Student(first_name='Rick',last_name='Morty',age='19')
myStudent3.print_name()