# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

# novo format so funciona com aspas duplas dentro do parenteses.

frase = str (input ('Digite uma frase: ')).lower().strip()
print (f'A letra a aparece {frase.count("a")} vezes na frase.')
# adicionar o +1 no final para nao aparecer a contagem apartir de zero
print (f'A primeira letra a apareceu na posição {frase.find("a")+1}')
# comando r na frente do find faz com que se comece a ler do right/da direita para a esquerda
print (f'A ultima letra a apareceu na posição {frase.rfind("a")+1}')
