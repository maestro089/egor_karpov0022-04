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
print(s)
