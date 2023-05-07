import math as m
w = 1
A = 1
B = -1

i = 1

x = 1       #Начальное приближение
x2 = -1

xi = 0
xi2 = 0

def f(x):        #Функция
    return (x**2+A*x+B)**2

def fd(x):       #Производная
    return 4*x**3 + 6*A*x**2 + 2*A**2*x + 4*B*x + 2*A*B

while w==1:
    xi = x - f(x)/fd(x)
    xi2 = x2 - f(x2)/fd(x2)
    print("Iteration:", i, "| x1 =", x, "|x2 =", x2,"| r =", abs(xi-x))
    if abs(xi-x) < 10**(-14):
        break
    else:
        x = xi
        x2 = xi2
        i+=1
