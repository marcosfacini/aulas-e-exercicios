# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.   

somador_idade = 0
maior_idade = 0
nome_velho = ''
contador_mulher = 0

for pessoas in range (1, 5):
    print (f'============== {pessoas}º PESSOA ===============: ')
    print (f'Qual é o nome da {pessoas}º pessoa?: ')          
    nome = str (input ('Digite o nome: '))
    idade = int (input ('Qual é a idade?: '))
    sexo = str (input ('Qual é o sexo? \nDigite M para masculino e F para feminino: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print ('Letra inválida. Digite M ou F. Tente novamente.')
        exit()

    somador_idade += idade
    
    # assume-se que o primeiro laço terá a maior idade, e consequentemente vai receber o nome de mais valho
    if pessoas == 1 and sexo == 'M':
        maior_idade = idade
        nome_velho = nome
    if idade > maior_idade and sexo == 'M':
        maior_idade = idade
        nome_velho = nome

    if sexo == 'F' and idade < 20:
        contador_mulher += 1


media = somador_idade / 4
print (f'A média de idade entre eles é: {media}')

print (f'O homem mais velho é o {nome_velho} com {maior_idade} anos.')

if contador_mulher == 0:
    print ('Não existem mulheres no grupo.')
elif contador_mulher == 1:
    print ('Existe apenas uma mulher com menos de 20 anos.')
else:
    print (f'Existem {contador_mulher} mulheres com menos de 20 anos.')

