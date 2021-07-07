""" # usando o while para a mesma função do for:
# se eu souber o limite, posso usar qualquer um dos dois
for contador in range (1, 10):
    print (contador)

contador = 1
while contador < 10:
    print (contador)
    contador += 1 """

# se eu não sei o limite, só o while vai resolver. 

# vai ficar eternamente no laço até que o input seja 0
""" n = 1
while n != 0:
    n = int (input ('Digite um número: '))
print ('FIM') """

# vai ficar eternamente no laço até que seja digitado algo diferente que a palavra SIM
""" resposta = 'SIM'
while resposta == 'SIM':
    numero = int (input ('Digite um número: '))
    resposta = str (input ('Quer continuar? Digite SIM ou NAO: ')).upper()
print ('FIM') """

# contando numeros pares e impares, e não somando o zero como par
n = 1
contador_par = 0
contador_impar = 0
# tem como informar as duas variaveis na mesma linha, visto que elas recebem o mesmo valor:
# ficaria assim: contador_par = contador_impar = 0
while n != 0:
    n = int (input ('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            contador_par += 1
        else:
            contador_impar += 1
print (f'Você digitou {contador_par} numeros pares e {contador_impar} numeros impares')

# "while True" cria um laço infinito
# "break" quebra o laço infinito e sai dele
# "continue" quebra o laço infinito, mas não sai dele, retorna para o inicio do laço infinito
# normalmente não é necessário usar o "continue" em um laço infinito
