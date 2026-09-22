import math
a=0.1
b=1.5
h=0.05
print("-"*25)
print(f"{'x':^10} | {'y':^10}")
print("-"*25)
steps=int(round((b-a)/h))+1
for i in range (steps):
    x=a+i*h
    part1=math.exp(math.asin(x/3))
    part2=1-math.exp(math.acos(x/4))
    y=part1+part2
    print(f"{x:^10.4f}|{y:^10.4f}")
    print("-"*25)