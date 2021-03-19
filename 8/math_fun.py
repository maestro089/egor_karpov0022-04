import math
import random


def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

def sum():
    print("a =")
    a = float(input())
    print("b = ")
    b = float(input())
    print(a+b)
    
def de():
    print("a =")
    a = float(input())
    print("b = ")
    b = float(input())
    print(a/b)
    
def node():
    print("a =")
    a = float(input())
    print("b = ")
    b = float(input())
    print(a*b)
        
def nosum():
    print("a =")
    a = float(input())
    print("b = ")
    b = float(input())
    print(a-b)
        
def s():
    print("a =")
    a = float(input())
    print("b = ")
    b = float(input())
    print(a ** b)
        
def mod():
    print("a =")
    a = float(input())
    print(math.fabs(a))
        
def acos():
    print("a =")
    a = float(input())
    print(math.acos(a))
    
def r():
    print("рандомное число в диапазона от = ")
    a = int(input())
    print("до =")
    b = int(input())
    print(random.randint(a,b))