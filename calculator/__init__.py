from calculator.operations import add, subtract, multiply, divide

'''Creates an Instance of the Calculation class'''
class Calculation:
    def __init__(self, a, b, operation):
        # Dunder method for object initialization
        self.a = a # property, stores value of a in an instance of this class
        self.b = b # property, stores value of b in an instance of this class
        self.operation = operation # property, stores the operation function

    def get_result(self):
        # Calls stored operation with a and b
        return self.operation(self.a, self.b)

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
