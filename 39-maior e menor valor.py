# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# solução com uma linha a menos ja considerando que um numero seja o menor e o outro o maior sem ele precisar passar pelo if
n1 = int (input ('Digite o primeiro número: '))
n2 = int (input ('Digite o segundo número: '))
n3 = int (input ('Digite o terceiro número: '))
menor = n1
maior = n2

# verificando o menor:
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3  

# verificando o maior:
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n2 and n3 > n1:
    maior = n3    

print (f'O menor número é {menor} e o maior número é {maior}') 


# jeito que eu tinha pensado:
""" n1 = int (input ('Digite o primeiro número: '))
n2 = int (input ('Digite o segundo número: '))
n3 = int (input ('Digite o terceiro número: '))

# verificando o menor:
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2    
if n3 <n1 and n3 < n2:
    menor = n3

# verificando o maior:
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print (f'A menor número é {menor} e o maior número é {maior}') """                






