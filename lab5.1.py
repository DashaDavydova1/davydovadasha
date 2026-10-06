import math
n = int(input ("Введите количество чисел N: "))
product=1.0
print (f"Введите{n}чисел:")
for i in range (n):
    num=float (input())
    product*=abs(num)
geom_mean=product ** (1 / n)    
print (f"Среднее геометрическое абсолютных величин: {geom_mean:.4f}")