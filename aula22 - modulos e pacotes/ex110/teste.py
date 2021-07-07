# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), 
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

import moeda

preço = float (input ('Digite o preço: '))
aumento = int (input ('Qual a porcentagem de aumento?: '))
desconto = int (input ('Qual a porcentagem de desconto?: '))
moeda.resumo(preço, aumento, desconto)


