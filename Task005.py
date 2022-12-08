# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*

with open ('text1.txt', 'r') as file_1:
    str_1=file_1.read()

with open ('text2.txt', 'r') as file_2:
    str_2=file_2.read()

str_1=str_1.split()
str_2=str_2.split()

mnogo_1=[]
mnogo_2=[]      

for i in range(len(str_1)):
    if str_1[i].isdigit():
        mnogo_1.append(str_1[i])

for i in range(len(str_2)):
    if str_2[i].isdigit():
        mnogo_2.append(str_2[i])     
 
res1=int(str_1[0]) + int(str_2[0])
res2=int(str_1[6]) + int(str_2[6])
res3=int(str_1[10]) + int(str_2[10])

str_res=(f"{res1}*x^2+{res2}*x+{res3}=0")

with open('text3.txt', 'w') as f:
    f.write(str_res)