

import moeda

preço = float (input ('Digite o preço: '))
print (f'{(preço)} com {10}% de aumento fica: {(moeda.aumentar(preço, 10))}')
print (f'{(preço)} com {10}% de desconto fica: {(moeda.diminuir(preço, 10))}')
print (f'O dobro de {(preço)} é: {(moeda.dobro(preço))}')
print (f'A metade de {(preço)} é {(moeda.metade(preço))}')


