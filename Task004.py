# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)* многочлена 
# и записать в файл многочлен степени k.
from random import randint

k=int(input("Введите натуральную степень К: "))
koef=[] # генерация списка коэффициентов
for i in range (0, k+1):
    koef.append(randint(0,101))
print(koef)

mnogo=[]

if k>=2:
    for i in range(0, k-1):
        if koef[i]==0:
            continue
        else:
            mnogo.append(f"{koef[i]} *x^ {k-i} +")
    if koef[-2]!=0:              
        mnogo.append((f"{koef[-2]} *x +"))
    if koef[-1]!=0:        
        mnogo.append(f'{koef[-1]}=0')
print(mnogo)

with open('text.txt', 'w') as f:
    f.write(f'-k={k} =>')
    for i in range(len(mnogo)):
        f.write(mnogo[i])
    

    