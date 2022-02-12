# in this file we can find complex calculations functions
# This is the next step to develop at the program
from math import sqrt
class Complex:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def sqrt_op(self):
        pass

    def exponential(self):
        # def compound_interest(self):
        pass

    def main(self):
        print("Select a operation:\n0 - Back\n1 - Sqrt\n2 - Exponential\n3 - Multiply\n4 - Divide\n")
        operation = int(input("Enter number (1/2): "))

        if operation == 1:
            self.num1 = float(input("Enter the first number: "))
            self.num2 = float(input("Enter the second number: "))

        elif operation == 2:
            nu1 = float(input("Enter the base: "))


        elif operation == 5:
            Complex()

        else:
            print("\nInvalid option!\n")
            return self.main()

        if operation == 1:
            self.sqrt_op()
        elif operation == 2:
            self.exponential()

        # elif operation == 3:
        #    self.multiply()
        # elif operation == 4:
        #    self.divide()

        # while True:
        #     verification = input("Calculate again? (y/n): ")
        #     if verification == "n": return 1
