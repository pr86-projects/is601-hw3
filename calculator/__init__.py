from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

'''Class with static methods. No instance is created.'''
class Calculator:
    @staticmethod
    def add(a,b):
        # This is a static method that pass the add function from calculator.operations
        calculation = Calculation(a, b, add)
        return calculation.get_result()
    @staticmethod
    def subtract(a,b):
        # This is a static method that pass the subtract function from calculator.operations
        calculation = Calculation(a, b, subtract)
        return calculation.get_result()
    @staticmethod
    def multiply (a,b):
        # This is a static method that pass the multiply function from calculator.operations
        calculation = Calculation(a, b, multiply)
        return calculation.get_result()
    @staticmethod
    def divide(a,b):
        # This is a static method that pass the divide function from calculator.operations
        calculation = Calculation(a, b, divide)
        return calculation.get_result()
