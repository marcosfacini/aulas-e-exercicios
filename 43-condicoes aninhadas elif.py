# pode-se colocar quantos elifs quiser
# o else é opicional, não obrigatorio
# O If serve para verificar uma condição e o elif serve para verificar outra condição caso a condição do If seja falsa. 
# No código não há muita diferença, o elif vai garantir que aquela condição seja verificada caso o If seja falso, 
# diferente dos dois If que são 'fluxos' independentes.
# so vai para o elif se o if for falso
# uma vantagem do elif é que Não precisamos indentar (dar espaço)! 
# Podemos colocar uma ELIF embaixo de outra ELIF e nosso código não fica tão extenso horizontalmente (e escrevemos menos).

char = str (input ('Escolha o seu personagem entre: guerreiro, cavaleiro, elfo, mago ou anão: ')).upper()
if char == 'GUERREIRO' or char == 'CAVALEIRO':
    print ('Personagens humanos são as escolhas mais comuns.')
elif char == 'ELFO':
    print ('Você vai se dar bem em alvos a distância!')
elif char == 'MAGO':
    print ('Você é apelão hein!!')
elif char == 'ANÃO':
    print ('Força e resistência sempre estarão com você!')        
else:
    print ('Personagem não reconhecido.')        

    # IMPORTANTE LEMBRAR QUE DEPOIS DO OPERADOR OR É NECESSÁRIO COLOCAR A VARIAVEL CHAR DE NOVO!!!