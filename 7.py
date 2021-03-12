

def fun(name):
    str_1 = []
    str_2 = []
    r = 0
    file = open(name + ".txt","r")#
    #заполняю массив строками
    for line in file:
        str_1.append(line)
    file.close
    file = open(name + ".txt","w")
    for key,val in str.items():
        file.write('{}:{}\n'.format(key,val))
    file.close
    file = open(name + ".txt","a")

    for i in range(len(str_1)):
        file.write(str_1[i])
    file.close

    file = open(name + ".txt","r")
    file.close
    
str = []
str_3 = []
print("Для выхода из цикла введите - quit")
while(True):
    check = input()
    if check == "quit":
        break
    else:
        str.append(check)
str_2 = set(str)
print("список -",str)
print("множество - ",str_2)
print("количество символов в cgbcrt =",len(str))
print("заполните следующий список из",len(str),"символов")
for i in range(len(str)):
    check = input()
    str_3.append(check)
print(str_3)
s = {str_3[i]:str[i] for i in range(len(str))}

print("Введите название файла")
name = input()

str = s

try:
    fun(name)
except IOError as e:
    file = open(name + ".txt","a")
    fun(name)


