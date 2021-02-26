str = input()
num = 0

for i  in range(0,len(str)):
    if str[i] == 'с':
        num = num +1
for i  in range(0,len(str) - 1):
    if i !=2 :
        print(str[i],end ='')
print("\n")
print("Символ 'с' встретился",num," раз")
