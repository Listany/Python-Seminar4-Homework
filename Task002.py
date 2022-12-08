# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num=int(input("Введите число: "))

num_lst=[]
while num>1:    
    if num%2==0:
        num=num/2
        num_lst.append(2)
    elif num%3==0:
        num=num/3
        num_lst.append(3)
    elif num%4==0:
        num=num/4
        num_lst.append(4)
    elif num%5==0:
        num=num/5
        num_lst.append(5)
    elif num%6==0:
        num=num/6
        num_lst.append(6)
    elif num%7==0:
        num=num/7
        num_lst.append(7)
    elif num%8==0:
        num=num/8
        num_lst.append(8)
    elif num%9==0:
        num=num/3
        num_lst.append(9)

print("Список простых множителей числа =", num_lst)
    