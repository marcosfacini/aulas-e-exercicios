# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

aluno = []
classe = []

while True:
    # poderia dar o input direto dentro do append(str (input ('Digite o nome: ')))
    nome = str (input ('Digite o nome: '))
    n1 = float (input ('Digite a primeira nota: '))
    n2 = float (input ('Digite a segunda nota: '))
    media = (n1 + n2) / 2
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    aluno.append(media)
    classe.append(aluno[:])
    aluno.clear()
    menu = str (input ('Deseja continuar? S/N: ')).strip().upper()[0]
    while menu != 'S' and menu != 'N':
        menu = str (input ('Letra Inválida. Digite S ou N: ')).strip().upper()[0]
    if menu == 'N':
        break

print (f'{"Nº":<4}', f'{"Aluno":<15}', f'{"Media":>5}')
for posicao, pessoa in enumerate(classe):
    print (f'{posicao:<4}', f'{pessoa[0]:<15}', f'{pessoa[3]:>5.1f}')

while True:
    opcao = int (input ('Deseja ver as notas de qual aluno? (ou digite 999 para finalizar): '))
    if opcao == 999:
        break
    while opcao > len(classe)-1:
        opcao = int (input ('Posição Inválida. Digite a posição correta ou 999 para encerrar: '))
        if opcao == 999:
            break
    
    print (f'As notas de {classe[opcao][0]} são: {classe[opcao][1]} e {classe[opcao][2]}')
    