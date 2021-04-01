def writing_file(name):
    
    mass_1 = []
    
    r = 0
    
    file = open(name + ".txt","r")
    
    #заполняю массив строками
    for line in file:
        mass_1.append(line)
    file.close
    file = open(name + ".txt","w")
    
    for key,val in dictionary.items():
        file.write('{}:{}\n'.format(key,val))
    file.close
    file = open(name + ".txt","a")

    for i in range(len(mass_1)):
        file.write(mass_1[i])
    file.close


    
mass = []
mass_3 = []

print("Для выхода из цикла введите - quit")

while(True):
    check = input()
    if check == "quit":
        break
    else:
        mass.append(check)
        
set_2 = set(mass)
print("список -",mass)
print("множество - ",set_2)
print("количество символов в cgbcrt =",len(mass))
print("заполните следующий список из",len(mass),"символов")

for i in range(len(mass)):
    check = input()
    mass_3.append(check)
    
print(mass_3)
s = {mass_3[i]:mass[i] for i in range(len(mass))}

print("Введите название файла")
name = input()

dictionary = s

try:
    writing_file(name)
except IOError as e:
    file = open(name + ".txt","a")
    writing_file(name)

