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
    

run = True
print("/ - деление \n* - умножение \n+ - сложение \n- - разность\nm - модуль\narccos - arccos \n^ - возведение в степень \n! - факториал \nrand - рандомное число \nquit - выход")

while(run):
    str = input()

    if str == "/":
        de()
        
    elif str == "quit":
        run = False
        
    elif str == "*":
        node()
        
    elif str == "-":
        nosum()
        
    elif str == "+":
        sum()
        
        
    elif str == "^":
        s()
        
    elif str == "m":
        mod()
        
    elif str == "arccos":
        print("a =")
        a = float(input())
        print(math.acos(a))
        
    elif str == "!":
        print("a =")
        a = float(input())
        print(factorial(a))
        
    elif str == "rand":
        print("рандомное число в диапазона от = ")
        a = int(input())
        print("до =")
        b = int(input())
        print(random.randint(a,b))
        
    else:
        print("Такой нет команды")
        
