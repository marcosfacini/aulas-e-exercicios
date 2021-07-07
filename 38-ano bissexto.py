# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# dentro da biblioteca datetime importei somente o date, e puxei o atributo .today e o .year dentro da mesma variavel ano

# operador != significa diferente de 

# operador and: Retorna True se todas as condições forem verdadeiras, caso contrário retorna False
# num > 1 and num < 5
# no caso acima o numero tem que ser maior que 1 E TAMBEM TEM QUE SER menor que 5 para retornar verdadeiro e aceitar a condição

# operador or: Retorna True se uma das condições for verdadeiras, caso contrário retorna False
# x > 1 or x < 5
# no caso acima o numero tem que ser maior que 1 OU TAMBEM PODE SER menor que 5 para retornar verdadeiro e aceitar a condição, só um dos precisa ser verdadeiro


from datetime import date
ano = int (input ('''Digite qual é o ano que deseja saber se é bissexto,
Digite 0 para analisar o ano atual: '''))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print (f'O ano {ano} é bissexto.')
else:
    print (f'O ano {ano} não é bissexto.')    
