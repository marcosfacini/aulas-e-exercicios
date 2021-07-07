# função anonima ou lambda é uma forma simplificada de declarar funções simples em uma unica linha
# é anonima porque essa função não recebe um nome
# Funções lambda funcionam da mesma forma que funções convencionais(def) 
# em geral, a escolha de adotar ou não seu uso é exclusivamente baseada em estilo de código.

# simplificando a função usando lambda, o resultado final será o mesmo, a diferença é que se usará menas linhas de código
def contador_letras(lista_palavras):
    contador = []
    for palavra in lista_palavras:
        quantidade = len(palavra)
        contador.append(quantidade)
    return contador


lista = ['cachorro', 'gato', 'macaco']
print (contador_letras(lista))

# com a lambda ficou com aapenas duas linhas
contador_lambda = lambda lista: [len(palavra) for palavra in lista] 
print (contador_lambda(lista))


# outro exemplo:
def soma(a, b):
    return a + b


print (soma(2, 3))

soma_lambda = lambda a, b: a + b
print (soma_lambda(2, 3))

