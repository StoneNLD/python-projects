#!/usr/bin/env python

from tire import Tire

class Car:
    """ 
    Car models a acar with tires and engine
    """ 

    #tires will be defined as strings, and not tire objects (Polymorphism)
    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    def description(self):
        print("A car with an {self.engine} engine, and {self.tires tires")

    #use function from tire (Composition)
    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0