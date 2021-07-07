m = float (input('Digite uma distância em metros: '))

print ('A medida de {:.2f}m corresponde a:'.format(m))

print ('{}km'.format(m/1000))
print ('{:.0f}cm'.format(m*100))
print ('{:.0f}mm'.format(m*1000))

# ou declarando as variáveis:

#km = m/1000
#cm = m*100 
#mm = m*1000

#print ('{}km'.format(km))
#print ('{}cm'.format(cm))
#print ('{}mm'.format(mm))