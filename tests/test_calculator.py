'''Testing the calculator class'''
from calculator import Calculator

def test_calculator_add():
    '''Testing the static add function'''
    assert Calculator.add(2,2) == 4
