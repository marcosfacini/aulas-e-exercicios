# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta,
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date
nascimento = int (input ('Em que ano você nasceu?: '))
atual = date.today().year
idade = atual - nascimento
if idade <= 9:
    print ('Sua categoriA é MIRIM')
elif idade <= 14:
    print ('Sua categoria é INFANTIL')    
elif idade <= 19:
    print ('Sua categoria é JÚNIOR')    
elif idade <= 25:
    print ('Sua categoria é SÊNIOR')    
else: 
    print ('Sua categoria é MASTER')    