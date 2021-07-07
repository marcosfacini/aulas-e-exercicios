from math import hypot
ca = float (input ('Qual é o cateto adjacente?: '))
co = float (input ('Qual é o cateto oposto?: '))
print (f'A hipotenusa é {hypot(ca, co):.2f}')

#import math
#ca = float (input ('Qual é o cateto adjacente?: '))
#co = float (input ('Qual é o cateto oposto?: '))
#print (f'A hipotenusa é: {math.hypot(ca, co):.2f}')

# com a formula matematica escrita:
# ca = float (input ('Qual é o cateto adjacente?: '))
# co = float (input ('Qual é o cateto oposto?: '))
# hip = (ca ** 2 + co ** 2) ** (1/2)
# print (f'A hipotenusa é: {hip:.2f}')