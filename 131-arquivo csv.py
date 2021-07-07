# O formato CSVé um arquivo de texto que representa dados em forma de tabela de forma simples.
# Cada linha do arquivo de texto é uma linha da tabela, e as colunas são separadas por vírgulas.

# biblioteca especifica para manipulação de arquivos de extensão .csv chamada csv
import csv

""" # usando o comando with para fechar o arquivo após a execução desse bloco
# comando "as" serve para dar um "apelido" ao arquivo 
with open('tabela.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv) # função reader() da biblioteca csv para ler a tabela
    cabeçalho = next(leitor) # comando next para fazer com que a leitura pule o primeira linha da tavela que é o cabeçalho e não contem numero para ser analisado pelo for abaixo
    for linha in leitor:
        if float(linha[2]) > 20:
            print (linha) """


""" with open('usuarios.csv', 'w', newline='') as arquivo_cadastro:
    escritor = csv.writer(arquivo_cadastro)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['marcos', 'facini', 'marcosgacini5@gmail.com', 'masculino']) """

header = ['nome', 'sobrenome']
dados = []
opcao = int (input ('Digite 1 para cadastrar e digite 0 para sair: '))

while opcao != 0:
    nome = str (input ('Primeiro nome: '))
    sobrenome = str (input ('Sobrenome: '))
    dados.append([nome, sobrenome])
    opcao = int (input ('Digite 1 para cadastrar e digite 0 para sair: '))

print (dados)

with open("usuarios.csv", 'w', newline='') as users: # parametro newline='' faz com que não se pule uma linha a cada linha escrita
    escrita = csv.writer(users)
    escrita.writerow(header)
    escrita.writerows(dados) # writerows escreve cada "sublista" da lista como uma linha

with open('usuarios.csv', 'r') as users:
    leitor = csv.reader(users)
    for linha in leitor:
        print (linha)

# existem outros parâmetros dentro da função open() que permitem editar a tabela como o:
# delimiter =  e o  lineterminator = 

# o abaixo eu ainda preciso estudar e testar:
""" DictReader e DictWriter
Podemos também trabalhar com dicionários, nos quais a primeira linha é lida como a chave e as demais são os respectivos valores:

with open('email.csv', 'r') as emails:
    leitor = csv.DictReader(emails, delimiter=';') #a primeira linha é lida como um cabeçalho
    for linha in leitor:
        print(linha['Login email']) #podemos chamar um valor específico de cada linha pela chave no cabeçallho


with open('names.csv', 'w', newline='') as csvfile:
    chaves = ['first_name', 'last_name'] # definimos o cabeçalho
    writer = csv.DictWriter(csvfile, fieldnames=chaves) # especificamos o cabeçalho

    writer.writeheader() # escrevemos o cabeçalho
    writer.writerow({'first_name': 'Senhor', 'last_name': 'Batata'}) # escrevemos linhas com as chaves e valores
    writer.writerow({'first_name': 'Will', 'last_name': 'Smith'})
    writer.writerow({'first_name': 'Elon', 'last_name': 'Musk'}) """

    