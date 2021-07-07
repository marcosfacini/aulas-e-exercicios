c = float (input ('Informe a temperatura em °C: '))
f = (c * 9 / 5) + 32

print ('A temperatura de {:.2f}°C corresponde a {:.2f}°F'.format(c,f))

# o conversor inverso ficaria assim:
#f = float (input ('Informe a temperatura em °F: '))
#c = (f - 32) * 5 / 9

#print ('A temperatura de {:.2f}°F corresponde a {:.2f}°C'.format(f,c))