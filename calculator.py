import math
import random
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

class BMICalculator(Calculator):
    def calculate_area(self):
        val = self.weight / (self.height * self.height)
        print(f'Your BMI is: {val:.2f}')
        if val >= 30:
            print('You are too heavy')
        elif val >= 25 and val < 30:
            print('You are overweight')
        elif val >= 18.5 and val < 25:
            print('You are normal')
        else:
            print('You are not overweight')
    def name(self):
        return 'BMI'
    def input(self):
        self.weight = float(input('Please input your weight:'))
        self.height = float(input('Please input your height:'))

class CollatzCalculator(Calculator):
    def calculate_area(self):
        num = self.number
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num * 3 + 1
            print(num)
            if num == 1:
                break
    def name(self):
        return 'Collatz'
    def input(self):
        self.number = int(input('Please input a number:'))

class GuessNumber(Calculator):
    def calculate_area(self):
        randomNum = random.randint(1, 100)
        times = 0
        for i in range(self.times):
            number = int(input('Please input a number:'))
            times += 1
            if number == randomNum:
                print(f'You guess the number with {times} times!')
                break
            elif number > randomNum:
                print('Your number is too big')
            else:
                print('Your number is too small')
    def name(self):
        return 'Guess Number'
    def input(self):
        print('Please guess the number which between 1 and 100')
        self.times = int(input('Please input the guess time limit:'))

class MultiTable(Calculator):
    def calculate_area(self):
        for i in range(1, 10):
            for j in range(1, i+1):
                print(f'{j} * {i} = {i * j}', end = '\t')
            print('')
    def name(self):
        return 'Multi Table'
    def input(self):
        pass

class Boat(Calculator):
    def calculate_area(self):
        print(f'Our location is {self.location}')
        print(f'We have {self.weapon} weapons and engines status is {self.engine} and {self.fuel} fuel')

        while True:
            action = input('Please choose the action [go, shoot, fuel, motor, exit]:')
            if action == 'go':
                if self.engine and self.fuel > 0:
                    print('You go!')
                    self.fuel -= 0.1
                else:
                    print('You can not go!')
            elif action == 'shoot':
                if self.weapon > 0:
                    self.weapon -= 1
                    print('You shoot the enemy!')
                else:
                    print('You have no weapon!')
            elif action == 'fuel':
                print(f'Your fuel is {self.fuel}')
            elif action =='motor':
                print(f'Your engine status is {self.engine}')
            elif action == 'exit':
                print('You exit the game!')
                break
            else:
                print('Please input a valid action!')
    def name(self):
        return 'Boat'
    def input(self):
        while True:
            username = input('Please input your name:')
            password = input('Please input your password:')
            if username == 'admin' and password == '123456':
                break
            else:
                print('Wrong username or password!')
        print('Welcome aboard!')
        self.location = 'Earth'
        self.weapon = 10
        self.engine = True
        self.fuel = 0.9

handlers = [CircleAreaCalculator(), RectangleAreaCalculator(),
            RightTriangleCalculator(), EngelsCoefficientCalculator(),
            BMICalculator(), CollatzCalculator(), GuessNumber(),
            MultiTable(), Boat()]
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
