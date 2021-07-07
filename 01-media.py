nota1 = int(input('insira primeira nota: ') )
nota2 = int(input('insira segunda nota: ') )
nota3 = int(input('insira terceira nota: ') )
nota4 = int(input('insira quarta nota: ') )

media = (nota1 + nota2 + nota3 + nota4) / 4
print ('sua média é:' , media)

if (media >= 5):
    print ('você passou de ano!')
else:
    print ('você reprovou!')


