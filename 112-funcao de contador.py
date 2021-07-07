# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# de 1 até 10, de 1 em 1
# de 10 até 0, de 2 em 2
# uma contagem personalizada

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print (cont, end=' ')
            cont += passo
        print ('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print (cont, end=' ')
            cont -= passo
        print ('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print ('Agora é a sua vez de personalisar a contagem: ')
begin = int (input ('Digite o início: '))
end = int (input ('Digite o fim: '))
pas = int (input ('Digite o passo: '))
contador(begin, end, pas)

# usando o for:
""" def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if inicio <= fim:
        for num in range(inicio, fim+1, passo):
            print(num, end = ' ')
        print ('FIM')

    else:
        for num in range(inicio, fim, -1):
            if num % 2 == 0:
                print(num, end = ' ')
        print('Fim')
            

contador(1, 10, 1)
contador(10, 0 , 2)
inicio = int (input ('Inicio: '))
fim = int (input ('Fim: '))
passo = int (input ('Passo: '))
contador(inicio, fim, passo) """