# This is where we can find the simple arithmetic functions
from math import sqrt
class Calculator:
    def __init__(self,number1,number2):
        self.num1 = number1
        self.num2 = number2

    def add(self):
        solution = self.num1 + self.num2
        resolution="{} + {} = {}".format(self.num1, self.num2, solution)
        return ["ADD",resolution]

    def subtract(self):
        solution = self.num1 - self.num2
        resolution = "{} - {} = {}".format(self.num1, self.num2, solution)
        return ["SUBTRACT",resolution]

    def multiply(self):
        solution = self.num1 * self.num2
        resolution="{} * {} = {}".format(self.num1, self.num2, solution)
        return ["MULTIPLY", resolution]

    def divide(self):
        solution = self.num1 / self.num2
        resolution="{} / {} = {}".format(self.num1, self.num2, solution)
        return ["DIVIDE", resolution]

    def sqrt_op(self):
        solution = sqrt(self.num1)
        resolution ="{}^(1/2) = {}".format(self.num1,solution)
        return ["SQRT", resolution]

    def exponential(self):
        solution = (self.num1)**self.num2
        resolution ="{}^{} = {}".format(self.num1, self.num2, solution)
        return ["EXPONENTIAL", resolution]
