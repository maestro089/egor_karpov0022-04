str = []
str_3 = []

def fun():
    str = []
    while(True):
        check = input()
        if check == "quit":
            break
        else:
            str.append(check)
    return str

def fun2(str):
    str_3 = []
    for i in range(len(str)):
        check = input()
        str_3.append(check)
    return str_3

def fun3(str_3,str):
    s = {str_3[i]:str[i] for i in range(len(str))}
    return s
    
    

print("Для выхода из цикла введите - quit")
str = fun()

str_2 = set(str)
print("список -",str)
print("множество - ",str_2)
print("количество символов в списке =",len(str))
print("заполните следующий список из",len(str),"символов")

str_3 = fun2(str)

print(str_3)
s = fun3(str_3,str)
print(s)
