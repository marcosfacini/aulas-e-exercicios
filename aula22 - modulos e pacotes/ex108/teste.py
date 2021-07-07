# Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
# que consiga mostrar os números como um valor monetário formatado.

import moeda

preço = float (input ('Digite o preço: '))
print (f'{moeda.moeda(preço)} com {10}% de aumento fica: {moeda.moeda(moeda.aumentar(preço, 10))}')
print (f'{moeda.moeda(preço)} com {10}% de desconto fica: {moeda.moeda(moeda.diminuir(preço, 10))}')
print (f'O dobro de {moeda.moeda(preço)} é: {moeda.moeda(moeda.dobro(preço))}')
print (f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')


