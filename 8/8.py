import math_fun as m


run = True
print("/ - деление \n* - умножение \n+ - сложение \n- - разность\nm - модуль\narccos - arccos \n^ - возведение в степень \n! - факториал \nrand - рандомное число \nquit - выход")

while(run):
    str = input()

    if str == "/":
        m.de()
        
    elif str == "quit":
        run = False
        
    elif str == "*":
        m.node()
        
    elif str == "-":
        m.nosum()
        
    elif str == "+":
        m.sum()
        
    elif str == "^":
        m.s()
        
    elif str == "m":
        m.mod()
        
    elif str == "arccos":
        m.acos()
        
    elif str == "!":
        print("a =")
        a = float(input())
        print(m.factorial(a))
        
    elif str == "rand":
        m.r()
        
    else:
        print("Такой нет команды")
        
