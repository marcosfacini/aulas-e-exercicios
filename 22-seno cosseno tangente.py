# é possível colocar um metodo dentro de outro: o metodo radians esta dentro do sin, cos e tan
from math import sin, cos, tan, radians
ang = float (input ('Qual é o angulo?: '))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print (f'O seno é {s:.2f} o cosseno é {c:.2f} e a tangente é {t:.2f}')


# chamando o modulo math em todas as variaveis:
# import math
# ang = float (input ('Qual é o angulo?: '))
# s = math.sin(math.radians(ang))
# c = math.cos(math.radians(ang))
# t = math.tan(math.radians(ang))
# print (f'O seno de {ang} é {s:.2f}, o cosseno é {c:.2f} e a tangente é {t:.2f}')