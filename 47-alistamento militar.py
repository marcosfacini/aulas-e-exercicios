# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
sexo = str (input ('''Qual é o seu sexo?
Digite M para masculino e F para feminino: ''')).upper()

if sexo =='M':    
    ano = int (input ('Digite o ano do seu nascimento: '))
    idade = atual - ano
    print (f'Quem nasceu em {ano} tem {idade} anos em {atual}')
    if idade < 18:
        saldo = 18 - idade
        anoalistamento = atual + saldo
        if saldo == 1:
            print (f'Você ainda precisa esperar {saldo} ano para se alistar.Seu alistamento será em {anoalistamento}')
        else:
            print (f'Você ainda precisa esperar {saldo} anos para se alistar.Seu alistamento será em {anoalistamento}')    
    elif idade == 18:
        print ('Você está na idade para o alistamento!')
    else:
        saldo = idade - 18
        anoalistamento = atual - saldo
        if saldo == 1:
            print (f'Já se passou {saldo} ano desde a data do seu alistamento. Você deveria ter se alistado em {anoalistamento}')  
        else:
            print (f'Já se passaram {saldo} anos desde a data do seu alistamento. Você deveria ter se alistado em {anoalistamento}')     

elif sexo == 'F':
    print ('Por ser do sexo feminino você não precisa se alisar.')     
else: 
    print ('Letra não reconhecida.')    