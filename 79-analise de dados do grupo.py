# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# quantas pessoas tem mais de 18 anos.
# quantos homens foram cadastrados.
# quantas mulheres tem menos de 20 anos. 

contador_idade = contador_homem = contador_mulher = 0

while True:
    idade = int (input ('Idade: '))
    sexo = str (input ('Sexo F/M: ')).strip().upper()[0]
    while sexo != 'F' and sexo != 'M':
        print ('Letra inválida. Digite novamente. F/M: ')
        sexo = str (input ('Sexo F/M: ')).strip().upper()[0]
    if idade >= 18:
        contador_idade += 1
    if sexo == 'M':
        contador_homem += 1
    if sexo == 'F' and idade < 20:
        contador_mulher += 1
    menu = str (input ('Deseja continuar? S/N: ')).strip().upper()[0]
    if menu != 'S' and menu != 'N':
        menu = str (input ('Letra Inválida. Digite S ou N: ')).strip().upper()[0]
    if menu == 'N':
        print ('Obrigado pelas informações.')
        break

print (f'Foram cadastradas {contador_idade} pessoas com mais de 18 anos.')
print (f'{contador_homem} homens.')
print (f'{contador_mulher} mulheres abaixo de 20 anos.')
