from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract,multiply, divide

'''Creates an Instance of the Calculation class'''
class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation):
        # Dunder method for object initialization
        self.a = a # property, stores value of a in an instance of this class
        self.b = b # property, stores value of b in an instance of this class
        self.operation = operation # property, stores the operation function

    def get_result(self):
        # Calls stored operation with a and b
        return self.operation(self.a, self.b)