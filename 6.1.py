mass_1 = []
mass_3 = []

def completion_mass_key():
    str = []
    while(True):
        check = input()
        if check == "quit":
            break
        else:
            str.append(check)
    return str

def completion_mass_values(str):
    str_3 = []
    for i in range(len(str)):
        check = input()
        str_3.append(check)
    return str_3

def completion_list(str_3,str):
    s = {str[i]:str_3[i] for i in range(len(str))}
    return s
    
    

print("Для выхода из цикла введите - quit")
mass_1 = completion_mass_key()

mass_2 = set(mass_1)
print("список -",mass_1)
print("множество - ",mass_2)
print("количество символов в списке =",len(mass_1))
print("заполните следующий список из",len(mass_1),"символов")

mass_3 = completion_mass_values(mass_1)

print(mass_3)
list = completion_list(mass_3,mass_1)
print(list)
