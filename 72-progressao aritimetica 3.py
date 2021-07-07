# Melhore o arquivo 71, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = int (input ('Primeiro termo: ')) 
razao = int (input ('Razão: '))
contador = 1
resultado = primeiro_termo
total = 0
a_mais = 10

while a_mais != 0:
    total = total + a_mais
    print ('Resultado = ', end='')
    while contador <= total:
        resultado += razao
        contador += 1
        print (resultado, end=' ')
    a_mais = int (input ('\nQuantos termos a mais você quer mostrar?: '))

print (f'Obrigado por jogar. Você consultou {total} termos.')


