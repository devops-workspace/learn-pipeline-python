import math
from abc import ABC

class Calculator(ABC):
    @classmethod
    def calculate_area(self):
        pass
    @classmethod
    def name(self):
        pass

    @classmethod
    def input(self):
        pass

class CircleAreaCalculator(Calculator):
    def calculate_area(self):
        pi = 3.14159
        print('The area of the circle is: ', pi * self.radius * self.radius)
    def name(self):
        return 'Circle'
    def input(self):
        self.radius = float(input('Please input the radius:'))

class RectangleAreaCalculator(Calculator):
    def calculate_area(self):
        print('The area of the rectangle is: ', self.length * self.width)
    def name(self):
        return 'Rectangle'
    def input(self):
        self.length = float(input('Please input the length:'))
        self.width = float(input('Please input the width:'))

class RightTriangleCalculator(Calculator):
    def calculate_area(self):
        print('The area of the right triangle is: ', math.sqrt(self.base * self.base + self.height * self.height))
    def name(self):
        return 'Right Triangle'
    def input(self):
        self.base = float(input('Please input the base:'))
        self.height = float(input('Please input the height:'))

class EngelsCoefficientCalculator(Calculator):
    def calculate_area(self):
        num = self.food / (self.education + self.food + self.medical + self.investment + self.unexpected)
        print(f'Your engels coefficient is: {num:.3f}')
    def name(self):
        return 'Engels Coefficient'
    def input(self):
        self.education = float(input('Please input your education spend:'))
        self.food = float(input('Please input your food spend:'))
        self.medical = float(input('Please input your medical spend:'))
        self.investment = float(input('Please input your investment spend:'))
        self.unexpected = float(input('Please input your unexpected spend:'))

handlers = [CircleAreaCalculator(), RectangleAreaCalculator(), RightTriangleCalculator(), EngelsCoefficientCalculator()]
for handler in handlers:
    print(handlers.index(handler), handler.name())

while True:
    try:
        index = int(input('Please choose the number of your desired caculator:'))
        if index < 0 or index >= len(handlers):
            print('Please input a valid number')
            continue
        handlers[index].input()
        handlers[index].calculate_area()
    except ValueError:
        print('Please input a valid number')
