sal = float (input ('Qual é o salário do funcionário?: R$'))
porc = float (input('Qual a porcentagem de aumento?: '))
sinal = "%"
total = (sal * porc / 100) + sal

print ('Um funcionário com salário de R${:.2f} que recebe {:.0f}{} de aumento, fica com o salário de R${:.2f}'.format(sal, porc, sinal, total))