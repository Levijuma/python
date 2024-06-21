class Student:
    def __init__(self,first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name

        #method

        def display(self):
            print(self.first_name, self.last_name)

#object
my_student=Student(first_name='John',last_name='Smith')
my_student.display()
my_student2=Student(first_name='Fortune',last_name='Ushindi')
my_student2.display()
