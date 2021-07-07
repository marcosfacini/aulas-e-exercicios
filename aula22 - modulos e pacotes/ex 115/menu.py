def linha(num):
    print ('=' * num)


def cabeçalho():
    linha(40)
    print (f'{"MENU PRINCIPAL":^40}')
    linha(40)
    print ('\033[1;33m1 =\033[0;0m \033[1;34mVer pessoas cadastradas \033[0;0m')
    print ('\033[1;33m2 =\033[0;0m \033[1;34mCadastrar nova pessoa \033[0;0m')
    print ('\033[1;33m3 =\033[0;0m \033[1;34mSair do sistema \033[0;0m')
    linha(40)

def opcao(texto):
    while True:
        try:
            m = int (input (texto))
            if m == 1:
                print ('=' * 40)
                print (f'{"PESSOAS CADASTRADAS":^40}')
                print ('=' * 40)
                return m
            elif m == 2:
                print ('=' * 40)
                print (f'{"NOVO CADASTRO:":^40}')
                print ('=' * 40)
                return m
            elif m == 3:
                print ('=' * 40)
                print (f'{"SAINDO DO SISTEMA...OBRIGADO E VOLTE SEMPRE":^40}')
                print ('=' * 40)
                return m
            elif m > 3 or m < 1:
                print ('=' * 40)
                print ('\033[1;31mERRO: Número inválido. Digite 1, 2 ou 3. \033[0;0m')
                print ('=' * 40)
        except:
            print ('\033[1;31mERRO: OPÇÃO INVÁLIDA \033[0;0m')

