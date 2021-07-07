# no tratamento do erro/excessão o else e o finally são opcionais
# o else só é executado quando o try não dá erro
# o finaly sempre é executado, o código dando errro ou não

""" try:
    a = int (input ('Digite o numerador: '))
    b = int (input ('Digite o denominador: '))
    r = a / b
except:
    print ('Ocorreu um erro.')
else:
    print (f'A resposta é: {r:.1f}')    
finally:
    print ('Obrigado e volte sempre.') """

# mostrando qual foi o erro de forma formatada:
""" try:
    a = int (input ('Digite o numerador: '))
    b = int (input ('Digite o denominador: '))
    r = a / b
except Exception as erro:
    print (f'Ocorreu um erro. O problema encontrado foi: {erro.__class__}')
else:
    print (f'A resposta é: {r:.1f}')
finally:
    print ('Obrigado e volte sempre.') """

# um mesmo try pode ter varios excepts
""" try:
    a = int (input ('Digite o numerador: '))
    b = int (input ('Digite o denominador: '))
    r = a / b
except Exception as erro:
    print (f'O erro encontrado foi: {erro.__cause__}')
except (ValueError, TypeError):
    print ('Ocorreu um erro com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print ('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print ('O usuário preferiu pular/sair da execução.')
else:
    print (f'A resposta é: {r:.1f}')
finally:
    print ('Obrigado e volte sempre.')
 """
# é possível criar uma classe de erro personalizada
# que deve ser herdada da classe Exception que já existe no python
# o comando "raise" força a execução do comando de excessões

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, mensagem):
        self.mensagem = mensagem

while True:
    try:
        n = int (input ('Digite um número entre 0 e 10: '))
        if n > 10:
            raise InputError('Opção Inválida. Você digitou um número maior que 10')
        elif n < 0:
            raise InputError('Opção Inválida. Você digitou um número menor que 0')
        break
    except InputError as ex:
        print (ex)

        






