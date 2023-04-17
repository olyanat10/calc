from math import sqrt, sin, degrees, cos, radians, tan
import decimal
from decimal import Decimal

l = 0
x = Decimal(input('x ='))
y = Decimal(input('y ='))
z = input()



if z == "+":
    l = x + y
    

elif z == "-":
    l = x - y
    

elif z == "*":
    l = (x * y)


elif z == "/":
    l = (x / y)


elif z == "%":
    l = (x % y)


elif z == "sqrt":
    l = f'{sqrt(x)},{sqrt(y)}'


elif z == "sin":
    l = f'{round(sin(radians(x)), 1)}, {round(sin(radians(y)), 1)}'


elif z == "cos":
    l = f'{round(cos(radians(x)), 1)}, {round(cos(radians(y)), 1)}'
    
elif z == "powpow":
    l = f'{round(pow(x, y))}, {round(pow(y, x))}'
print(l)