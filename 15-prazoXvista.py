# Calcular o preço do produto que a vista tem 5 por cento de desconto e a prazo tem acrescimo de 10 por cento

prod = float (input ('Qual é o preço do produto?: R$'))
vista = prod - (prod * 5 / 100) 
prazo = prod + (prod * 10 / 100)

print ('O preço a vista é: R${:.2f}'.format(vista))
print ('O preço a prazo é: R${:.2f}'.format (prazo))