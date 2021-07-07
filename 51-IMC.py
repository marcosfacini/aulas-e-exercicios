# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float (input ('Qual é o seu peso em kilos?: '))
altura = float (input ('Qual é a sua altura em metros?: '))
IMC = peso / altura ** 2
print (f'Seu IMC é de: {IMC:.1f} que se enquadra na categogia:' , end=' ')
if IMC < 18.5:
    print ('Abaixo do peso')
elif IMC <= 25:
    print ('Peso ideal')    
elif IMC <= 30:
    print ('Sobrepeso')
elif IMC <= 40:
    print ('Obesidade')    
else:
    print ('Obesidade mórbida')    