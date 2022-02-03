print("Welcome to my simple calculator!\n")
class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def add(self):
        solution=self.num1+self.num2
        print("{} + {} = {}".format(self.num1,self.num2,solution))

    def subtract(self):
        solution = self.num1 - self.num2
        print("{} - {} = {}".format(self.num1, self.num2, solution))

    def multiply(self):
        solution = self.num1 * self.num2
        print("{} * {} = {}".format(self.num1, self.num2, solution))

    def divide(self):
        solution = self.num1 / self.num2
        print("{} / {} = {}".format(self.num1, self.num2, solution))

    def main(self):
        print("Select a operation:\n1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide")
        operation=int(input("Enter number (1/2/3/4): "))
        if operation in [1,2,3,4]:
            nu1 = float(input("Enter the first number: "))
            nu2 = float(input("Enter the second number: "))
            self.num1 = nu1
            self.num2 = nu2

        else:
            print("\nInvalid option!\n")
            return self.main()

        if operation == 1: self.add()
        elif operation == 2: self.subtract()
        elif operation == 3:self.multiply()
        elif operation == 4: self.divide()

        while True:
            verification=input("Calculate again? (y/n): ")
            if verification=="n": return 1


while True:
    if Calculator().main(): break