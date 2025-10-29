class Person:
    def __init__(self, age=0):
        self._age = age

    def set_age(self, age):
        if age <= 0:
            print("age can not be negative, try again")
        else:
            self._age = age

    def get_age(self):
        return f"{self._age} years old"


p = Person()
p.set_age(25)
print(p.get_age())
p.set_age(-5)




class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"i am an animal"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"woof"
    def name(self):
        return f"{self.name}"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def name(self):
        return f"{self.name}"

    def speak(self):
        return f"meow"
cat = Cat("Kitty")
dog = Dog("Buddy")
print(dog.name, dog.speak())
print(cat.name, cat.speak())



class Vehicle:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def move(self):
        return 'vehicle is moving'


class Car(Vehicle):
    def move(self):
        return 'car is moving'

class Bicycle(Vehicle):
    def move(self):
        return 'bicycle is pedaling'

def move(vehicle):
    return vehicle.move()


car = Car('BMW')
bike = Bicycle('BMX')
print(move(bike))
print(move(car))


from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass



class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())    # Вывод: 50
print(round(circle.area(), 2))