# Crie um módulo chamado dado. 
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(), 
# mas com uma validação de dados para aceitar apenas valores que seja monetários, aceitando a virgula tambem

import moeda
from dado import leiaDinheiro

preço = leiaDinheiro('Digite o preço: ')
aumento = int (input ('Qual a porcentagem de aumento?: '))
desconto = int (input ('Qual a porcentagem de desconto?: '))
moeda.resumo(preço, aumento, desconto)


