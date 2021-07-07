# Vamos criar um menu em Python, usando modularização.

import menu
import manipulação

arquivo = manipulação.arquivoExiste("texto.txt")

menu.cabeçalho()
escolha = menu.opcao('\033[1;33mQual é a sua opção?: \033[0;0m')
while True:
    if escolha == 1:
        manipulação.lerArquivo(arquivo)
        escolha = menu.opcao('\033[1;33mQual é a sua opção?: \033[0;0m')
    if escolha == 2:
        nome = str (input ('Nome: '))
        idade = int (input ('Idade: '))
        manipulação.cadastrar(arquivo, nome, idade)
        escolha = menu.opcao('\033[1;33mQual é a sua opção?: \033[0;0m')
    if escolha == 3:
        break






