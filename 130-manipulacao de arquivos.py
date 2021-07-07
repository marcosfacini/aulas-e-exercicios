# metodo open() abre o arquivo, caso ele não exista ele cria o arquivo com o novo passado como parametro
# o segundo parametro é uma letra


""" # w = write - escreve algo no arquivo, caso já tenha algo escrito, ele vai escrever por cima
arquivo = open('teste.txt', 'w')
arquivo.write('Ola Mundo!')
arquivo.close()

# a = escreve algo no arquivo como continuação, sem apagar o que já tinha. e caso o arquivo não exista, ele também cria
arquivo = open('teste.txt', 'a')
arquivo.write('\nCurso de Python')
arquivo.close()

# r = read - lê o arquivo 
arquivo = open('teste.txt', 'r')
print (arquivo.read()) """

# é possível criar o arquivo em outra pasta fora da pasta em que você está chamando a criação dele
""" file = open('C:/Users/Marcos/Desktop/texto.txt', 'w')
file.write('Challenge Everithing!')
file.close() """

# exemplo:
alunos = open('notas.txt', 'w')
alunos.write('Felipe, 2, 4, 5\nRafael, 7, 9, 8\nJoao, 1, 4, 3')
alunos = open('notas.txt', 'r')
ler_arquivo = alunos.read()
separar = ler_arquivo.split('\n') # metodo split() separa os elementos pelo caracter que foi passado como parametro, e cria uma lista

for linha in separar:
    separacao = linha.split(',') # metodo split() separa os elementos pelo caracter que foi passado como parametro, e cria uma lista
    print (f'Nome: {separacao[0]}')
    separacao.pop(0) # retirando o primeiro elemento da lista, que nesse caso é o nome
    print (f'Notas: {separacao}')
    inteiros = []
    for n in separacao:
        inteiros.append(int(n)) # convertendo cada numero de string para inteiro
    media = sum(inteiros) / 3
    print (f'Média: {media:.1f}')
    
# copiar arquivo com o metodo shutil
# e possivel escolher aonde o arquivo copiado vai ser salvo, colocando o endereço no segundo parametro
import shutil
#shutil.copy('notas.txt', 'C:/Users/Marcos/Desktop/')

# é possivel escolher um outro nome para esse arquivo que será salvo, colocando o nome no final do endereço de destino
# shutil.copy('notas.txt', 'C:/Users/Marcos/Desktop/copia das notas.txt')

# para mover o arquivo para outra pasta/lugar
# nesse caso removeria o arquivo dessa pasta e o colaria na area de trabalho
# essa função é similar ao Control + x do Windows que recorta e cola
# shutil.move('notas.txt', 'C:/Users/Marcos/Desktop/')

# é possivel escolher um outro nome para esse arquivo que será movido, colocando o nome no final do endereço de destino
# shutil.move('notas.txt', 'C:/Users/Marcos/Desktop/copia das notas.txt')

# é importante sempre fechar o arquivo que foi aberto para salvar as alterações feitas e evitar bugs

# comando with fecha o arquivo no final da execução do bloco
# isso evita de esquecer de colocar o close() no final da execução
with open('teste.txt', 'r') as arquivolido:
   dados = arquivolido.read()
   print(dados)

# É possível ler o arquivo linha a linha
with open('teste.txt', 'r') as arquivolido:
   linha = arquivolido.readline()
   while linha != '':
       print(linha, end='')
       linha = arquivolido.readline()

# ou usando o for
with open('teste.txt', 'r') as arquivolido:
    for linha in arquivolido:
        print(linha, end='')

# O mesmo pode ser feito para escrever no arquivo
# as linhas do arquivo "teste.txt" são copiadas e salvas no arquivo "copiateste.txt".
with open('teste.txt', 'r') as arquivolido:
    with open('copiateste.txt', 'w') as arquivocriado:
        for linha in arquivolido:
            arquivocriado.write(linha)
    

# outro exemplo de arquivo manipulado está no arquivo ex 115 na pasta aula22-modulos e pacotes
