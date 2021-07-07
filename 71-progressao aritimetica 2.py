# Refaça o arquivo 60, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

# 3 e 2 = 3 5 7 9 11 13 15 17 19 21

primeiro_termo = int (input ('Digite o primeiro termo: '))
razao = int (input ('Digite a razao: '))
resultado = primeiro_termo
contador = 10

print (f'Progressão de {primeiro_termo} em {razao} é: ', end='')
while contador > 0:
    resultado += razao
    contador -= 1
    print (resultado, end=' ')




