# Reescreva a função leiaInt() que fizemos no arquivo 119, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(texto):
    ref = False
    while ref == False:
        try: 
            num = int (input (texto))
        except (ValueError, TypeError):
            print ('Opção inválida.')
        else:
            ref = True
    return num


""" def leiaFloat(texto):
    ref = False
    while ref == False:
        try: 
            num = float (input (texto))
        except (ValueError, TypeError):
            print ('Opção inválida.')
        else:
            ref = True
    return num """

# usando o operador continue:
# mas a função e o laço funcionariam normalmente sem o continue
def leiaFloat(texto):
    while True:
        try: 
            num = float (input (texto))
        except (ValueError, TypeError):
            print ('Opção inválida.')
            continue
        except KeyboardInterrupt:
            print ('\nO usuário preferiu pular/sair da execução.')
            return 0 # o return tem a função de também quebrar o laço semelhante ao break
        else:
            return num



n = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número decimal: ')
print (f'Você acabaou de digitar os número: {n} e {f}')