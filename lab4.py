import math
S=0
for n in range (1, 31):
    numerator=(0.4 ** n) * math.cos((n*math.pi)/4)
    denominator = math.factorial(n+2)
    S += numerator / denominator 
    print (f"Сумма S= {S:.10f}")