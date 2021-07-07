# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velo = float (input ('Qual é a velocidade do seu carro?: '))
if velo > 80:
    print ('Você foi multado!')
    multa = (velo - 80) * 7
    print (f'Você vai pagar R$ {multa:.2f} de multa.')
else:
    print ('Parabéns! Continue dirigindo com segurança.')
print ('Tenha um bom dia!')    
