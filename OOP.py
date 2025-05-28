# Polymorphism
# What is polymorphism?

# Example Three: Polymorphism with inheritance
# Superclass
class Bird:
    def fly(self):
        print('Birds flies in the sky')


# derived class
class Eagle(Bird):
    def fly(self):
        print('Eagle flies at high altitude')


class Sparrow(Bird):
    def fly(self):
        print('Sparrow flies at low altitude')


# How we use polmorphism
def flight_test(bird):
    bird.fly()  # Run respective class method based on an object


# Create objects
eagle1 = Eagle()
sparrow1 = Sparrow()

# Call the flight test method with diffrent objects

flight_test(eagle1)
flight_test(sparrow1)

#importing the ABC module to create an abstract class
from abc import ABC, abstractmethod #Abstraction


#starting a car engine and bike 
#define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass #this method start has no implementation in the abstract class
    #child class implementing the abstract method
class Car(Vehicle):
    def start(self):
        print("Car engine started")
#Derive class implementing the abstract method
class Bike(Vehicle):
    def start(self):
        print("Bike engine started")
#we cannot create objects of the abstract class
#demo live:
# vehicle = Vehicle()  # This will raise an error because Vehicle is abstract
# Create objects of the derived classes
car1 = Car()
bike1 = Bike()
#display the output of the methods we would use
#calling the start method on the objects
car1.start()  # Output: Car engine started
bike1.start()  # Output: Bike engine started

#submit your work on github for method overriding and method overloading and MRO
#MRO 