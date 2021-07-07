# Cada letra da string corresponde a um número e a contagem começa no zero
frase = 'Olá Mundo!'
print (frase [4])

# os dois pontos fazem uma seleção da letra 4 até a letra 8 a letra 9 não entra, tem que colocar um numero a mais mesmo
print (frase [4:9])

# adicionando mais um dois pontos, faz que apenas exiba as letras de duas em duas
print (frase [0:9:2])

# nao é necessário colocar o numero zero quando se quer que se exiba desde o começo da string
print (frase[:5])

# da mesma forma não é necessário colocar o numero da ultima letra se for para exibir até o final da string
print (frase[3:])

# não é necessário colocar o numero do meio também, já se entende que é até o final da string
print (frase[0::3])

# comando len mostra o cumprimento da string
print (len(frase))

# conta quantos caracteres informados tem dentro da string
print (frase.count('o'))

# pode-se indicar aonde começa e aonde termina a busca pelo caractere específico
print (frase.count('O',0,10))

# indica em que caractere começa a letra ou palavra entre parenteses
print (frase.find('Mundo'))

# comando in verifica se existe a letra ou palavra dentro da string e retorna com True ou False
print ('Olá' in frase)

# substitui por outra palavra
print (frase.replace('Mundo','Terra'))
# comando replace apenas substitui temporariamente, para substituir o conteudo de uma string definitivamente,
# precisa-se atribuir um novo valor a essa string
# frase = 'Olá Mundo!' 
# frase = frase.replace('Mundo' , 'Terra')
# print (frase)

# letras maiusculas
print (frase.upper())

# letras minusculas
print (frase.lower())

# deixa só a primeira letra da string maiuscula
print (frase.capitalize())

# deixa todo inicio de palavra maiusculo
teste = 'gosto muito de programar'
print (teste.title())

# remover os espaços do inicio e do final da string
teste2 = '    Código fonte    '
print (teste2.strip())

# remove apenas os espaços da direita/final da string    
# letra r de right/direita antes do metodo strip
print (teste2.rstrip())

# remove apenas os espaços da esquerda/inicio da string    
# letra l de left/esquerda antes do metodo strip
print (teste2.lstrip())

# separa todas as palavras de uma string, formando uma lista com elas, que se inicia a contagem apartir do numero 0
print (frase.split())
# é possivel somente a palavra que corresponde a lista 1 entre colchetes e somente a letra que corresponde ao segundo colchete
dividido = frase.split()
print (dividido [1] [2])

# 3 aspas duplas faz com que você consiga imprimir o texto todo sem precisar executar varias vezes o comando print
print ("""jcnjncjnjnckejsnjnjnjknsjkcnjkncjknjkcnjkrnjnrkcnnrkujnukukncjkcn
b xhjbjhcbhjsbnchbhsbhbrhcjbrhbhbchkbshckbhcbhsbhbch
cb hjbhjcbhjbchjsrbchjbhjcbhjbchjsbhcjbrhjcb
jcnncrkhnhkcnkhnchknhknchnhkcnrkchnsrhkcn
cnhknchknhkcnhksncchjckhnknjn""")

# une palavras atraves de um caractere especificado dentro das aspas simples
frase3 = ('maca', 'banana', 'abacate', 'pera')
print ('-'.join(frase3))

#é possível exibir a frase ao contrário com o comando -1
frase = 'Eu amo bolo'
invertida = frase[::-1]
print (invertida)