'''Actual implementation of the operations'''
from decimal import Decimal

def add(a: Decimal, b: Decimal):
    return a + b

def subtract(a: Decimal, b: Decimal):
    return a - b

def multiply(a: Decimal, b: Decimal):
    return a * b

def divide(a: Decimal, b: Decimal):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
