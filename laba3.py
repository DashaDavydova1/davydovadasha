import math

x=3.2

a=(x**3) *((math.tan((x+5)**2))**2)

b= 4*(x**(1/3))

c=math.sqrt(math.sin(x)+(math.pi/2))

d=b/c

y=a+d

print(f'{y:.5f}') 
