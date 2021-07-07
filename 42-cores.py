# consultar tabela de cores para saber os codigos
# inserir codigo dentro do print dentro das aspas
# o codigo começa com \033[ e termina com a letra m
# primeiro codigo para o estilo da letra, segundo codigo para cor do texto e terceiro codigo para cor do fundo, separados por ponto e virgula
# os padrões começam com 30 para cor do texto e começam com 40 para as cores do fundo
# existe uma biblioteca que tem muito mais funcionalidades e cores chamada colorize

#print ('\033[1;34;45mOlá Mundo!')

#print ('\033[0;36;41mOlá Mundo!')

# codigo vazia retorna ao padrão original
print ('\033[mOlá Mundo!')

# é possivel colocar os codigos de cor dentro do format para separar melhor do texto
a = 3
b = 6
print ('O numero {}{}{} e o número {}{}{}'.format('\33[34m' , a , '\33[m' , '\33[31m' , b , '\33[m'))