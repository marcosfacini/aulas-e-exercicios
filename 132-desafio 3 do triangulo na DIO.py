# desafio 3 triângulo da Dio
# para a platagorma aceitar as entradas de valores, eles devem ser colocados dentro de uma lista e depois separados em variaveis

x = [float(x) for x in input().split()]
A = x[0]
B = x[1]
C = x[2]

if A < B + C and B < A + C and C < A + B: 
    print(f"Perimetro = {A + B + C:.1f}")
else:
    area = (A + B) * C / 2
    print(f"Area = {area:.1f}")