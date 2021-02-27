import math
import random

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

run = True
print("/ - деление \n* - умножение \n+ - сложение \n- - разность\nm - модуль\narccos - arccos \n^ - возведение в степень \n! - факториал \nrand - рандомное число \nquit - выход")

while(run):
    str = input()

    if str == "/":
        print("a =")
        a = float(input())
        print("b = ")
        b = float(input())
        print(a/b)
        
    elif str == "quit":
        run = False
        
    elif str == "*":
        print("a =")
        a = float(input())
        print("b = ")
        b = float(input())
        print(a*b)
        
    elif str == "-":
        print("a =")
        a = float(input())
        print("b = ")
        b = float(input())
        print(a-b)
        
    elif str == "+":
        print("a =")
        a = float(input())
        print("b = ")
        b = float(input())
        print(a+b)
        
    elif str == "^":
        print("a =")
        a = float(input())
        print("b = ")
        b = float(input())
        print(a ** b)
        
    elif str == "m":
        print("a =")
        a = float(input())
        print(math.fabs(a))
        
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
        
