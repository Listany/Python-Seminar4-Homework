# Вычислить число Пи c заданной точностью d
from math import pi

d=(input()).split(".")
acc=len(d[1])+2 # длина строки Пи
print(str(pi)[0:acc])
