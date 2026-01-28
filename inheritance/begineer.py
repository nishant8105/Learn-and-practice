print('''1️⃣ Animal Sound System
Create a base class Animal with:
method: make_sound()
Create child classes:
Dog
Cat
Each child should override make_sound().''')

class Animal:
    def make_sound(self):
        print("Sound of animal")

class Dog(Animal):
    def make_sound(self):
        return "Dog is barking"

class Cat(Animal):
    def make_sound(self):
        return "Cat is meowing"

animal = Animal()
animal.make_sound()
dog = Dog()
print(dog.make_sound())
cat = Cat()
print(cat.make_sound())

print('''2️⃣ Vehicle Hierarchy
Create a base class Vehicle with:
method: start()
Create child classes:
Car
Bike
Each child prints its own start message.''')

class Vehicle:
    def start(self):
        return "Vehicle start"
    
class Car (Vehicle):
    def car_start(self):
        return "Car start"
class Bike (Vehicle):
    def bike_start(self):
        return "Bike start"

van = Vehicle().start()
print(van)
car = Car().car_start()
print(car)
car = Car().start()
print(car)
bike = Bike().bike_start()
print(bike)
bike = Bike().start()
print(bike)

print('''3️⃣ Employee System
Create a base class Employee with:
attributes: name, salary
method: get_details()
Create a child class Manager that
adds attribute: bonus
overrides get_details().''')

class Employee :
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_details(self):{
print(f'''Employee details
Name : {self._name}
Salary : {self._salary}''')
}

class Manager(Employee) :
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bouns = bonus
    
    def get_details(self):{
print(f'''Employee details
Name : {self._name}
Salary (bouns) : {self._salary + self.bouns}''')
}

        
# e1 = Employee("Nishant",90000)
# e1.get_details()
manager = Manager("Nishant",90000,8000)
manager.get_details()
print('''4️⃣ Shape Area Calculator
Create a base class Shape with:
method: area()
Create child classes:
Rectangle
Circle
Each child calculates its own area.''')
import math
class Shape :
    def area (self):
        pass

class Rectangle :
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_ractangle (self):
        area = self.width * self.height
        return area

class Circle :
    def __init__(self, radius):
        self.radius = radius
    
    def area_circle(self):
        area = 2 * math.pi * self.radius
        return round(area, 2)

rect = Rectangle(42, 62)
print("Area of rectangle : ",rect.area_ractangle())
circle = Circle(5)
print("Area of circle : ",circle.area_circle())