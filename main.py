print("Welcome to py-simple-calculator!\n")
# Here is the core of the program, management of the operations
# from complex import Complex
import os
from register import Calculator
os.system('clear')
class Menu:
    def __init__(self):
        self.historic = []
        self.num1 = 0
        self.num2 = 0

    # Here we'll see the resolution of the last calculation
    def result(self):
        if len(self.historic)>0:
            print("\n   Resolution:\n   {}\n".format(self.historic[-1][1]))

    def action(self):
        while True:
            verification = input("Calculate again? (y/n): ")
            if verification == "n":
                break
            elif verification == "y":
                os.system('clear')
                return self.basic()

    # Management of the basics operations
    def basic(self):
        print("Select a operation:\n0 - History\n1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide\n5 - More options (UNDER DEVELOPMENT!)")
        operation = int(input("Enter number (1/2/3/4): "))

        if operation in [1, 2, 3, 4]:
            self.num1 = float(input("Enter the first number: "))
            self.num2 = float(input("Enter the second number: "))

        #elif operation == 5: Complex()

        if operation == 0:
            print()
            for c in self.historic:
                print("   {}: {}".format(c[0], c[1]))
            print()
            return self.basic()

        elif operation == 1:
            self.historic.append(Calculator(self.num1,self.num2).add())
        elif operation == 2:
            self.historic.append(Calculator(self.num1,self.num2).subtract())
        elif operation == 3:
            self.historic.append(Calculator(self.num1,self.num2).multiply())
        elif operation == 4:
            self.historic.append(Calculator(self.num1,self.num2).divide())
        elif operation == 5:
            return self.complex()
        else:
            print("\nInvalid option!\n")
            return self.basic()
        self.result()
        self.action()

    def complex(self):
        print("Select a operation:\n0 - Back\n1 - Sqrt\n2 - Exponential\n")
        operation = int(input("Enter number (1/2): "))

        if operation == 0:
            return self.basic()

        elif operation == 1:
            self.num1 = float(input("Enter the number: "))
            self.historic.append(Calculator(self.num1, 0).sqrt_op())

        elif operation == 2:
            self.num1 = float(input("Enter the base: "))
            self.num2 = float(input("Enter the exponent: "))
            self.historic.append(Calculator(self.num1, self.num2).exponential())

        else:
            print("\nInvalid option!\n")
            return self.basic()

        self.result()
        self.action()

if __name__ == '__main__':
    Menu().basic()