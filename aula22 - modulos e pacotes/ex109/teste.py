# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

# criei um novo parametro opcional chamado change, que por padrão é false, ou seja não mostra a formatação

import moeda

preço = float (input ('Digite o preço: '))
print (f'{moeda.moeda(preço)} com {10}% de aumento fica: {(moeda.aumentar(preço, 10, True))}')
print (f'{moeda.moeda(preço)} com {10}% de desconto fica: {(moeda.diminuir(preço, 10, True))}')
print (f'O dobro de {moeda.moeda(preço)} é: {(moeda.dobro(preço, True))}')
print (f'A metade de {moeda.moeda(preço)} é {(moeda.metade(preço, True))}')


