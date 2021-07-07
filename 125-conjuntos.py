# conjuntos são um grupo de dados que não se repetem
# ficam dentro de chaves {} assim como os dicionários, porém não recem os dois valores de key e value igual ao dicionário

""" # nesse caso irá retirar os elementos repitidos
conjunto = {1, 1, 2, 2, 3}

# adicionar elemento ao conjunto
conjunto.add(5)

# remover elemento
conjunto.discard(2) """

""" # unindo conjuntos, o numero 5 só vai aparecer uma vez
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto1.union(conjunto2)

# pode-se isolar apenas o numero que se repete, nesse caso o 5
conjunto_repete = conjunto1.intersection(conjunto2)

# imprimir apenas os elementos que não se repetem, ou seja nesse caso, só não imprimiria o 5 porque se repete nos dois conjuntos
conjunto_diferença1 = conjunto1.difference(conjunto2)
print (conjunto_diferença1)
conjunto_diferença2 = conjunto2.difference(conjunto1)
print (conjunto_diferença2)

# imprimindo apenas os numeros que não se repetem, o contrario do metodo intersection()
# nesse caso, só não imprime o numero 5
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print (conjunto_diff_simetrica) """

# subset significa subconjunto, ou seja, todos os elementos do subconjunto estão no conjunto maior
# chamado superset, mas nem todos os elementos do superset estão no subset
""" conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print (conjunto_subset)
conjunto_superset = conjunto_b.issuperset(conjunto_a) """

# convertendo uma lista para conjunto para tirar a duplicidade dela
lista = ['macaco', 'pato', 'cachorro', 'pato', 'cachorro']
lista_conjunto = set(lista)
print (lista_conjunto)

# convertendo conjunto para lista
lista_editada = list(lista_conjunto)
print (lista_editada)