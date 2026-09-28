import math
P=1
for n in range (1,21):
    numerator = math.sin(2 * (n ** n) + 2 * n + 1)
    denominator = math.cos(n ** 2 + 1)
    P *= numerator / denominator
print (f" Произведение P= {P:.10f}")