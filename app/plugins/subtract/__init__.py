from app.commands import Command
from calculator import Calculator
from decimal import Decimal

class SubtractCommand(Command):
    def execute(self, *args):
        try:
            num1 = Decimal(args[0])
            num2 = Decimal(args[1])
        except:
            print("Please enter a valid number")
            return
        try:
            print(f"The result is: {Calculator.subtract(num1, num2)}")
        except ValueError as e:
            print(e)
