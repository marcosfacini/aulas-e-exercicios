# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

# usando a função titulo() dentro da função ajuda()
def ajuda(comando):
    titulo('Segue as informações: ')
    return help(comando)

def titulo(texto):
    print ('\033[1;42m=' * len(texto))
    print (texto)
    print ('=' * len(texto))
    print('\033[0;0m')


while True:
    nome_comando = str (input ('\033[1;43mDigite o comando ou FIM para encerrar: \033[0;0m')).strip()
    titulo('Analisando o comando...')
    if nome_comando.upper() == 'FIM':
        print ('\033[1;41mObrigado e volte sempre.\033[0;0m')
        break
    else:
        print (f'\033[1;104m{ajuda(nome_comando)}\033[0;0m')
    


