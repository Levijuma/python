class Animal:
    def speak(self):
        print('Animal is speaking')

class Dog(Animal):
    def bark(self):
        print('Dog is barking')

class Cat(Animal):
    def meow(self):
        print('Cat is meowing')

class Snake(Animal):
    def hiss(self):
        print('Snake is hissing')

d=Dog()
d.bark()
c=Cat()
c.meow()
s=Snake()
s.hiss()
d.speak()