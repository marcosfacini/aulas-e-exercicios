def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
        print('Arquivo já existe')
        return nome
    except:
        print ('Arquivo não existente. Criando arquivo....')
        criarArquivo(nome)
        return nome
    

def criarArquivo(nome):
    arquivo = open(nome, 'wt+')
    arquivo.close()


def lerArquivo(nome):
    arquivo = open(nome, 'rt')
    for linha in arquivo:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print (f'{dado[0]:<25}{dado[1]:>10} anos')
    arquivo.close()

def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        file = open(arquivo, 'at')
    except:
        print ('Houve um erro ao abrir o arquivo.')
    else:
        try:
            file.write(f'{nome};{idade}\n')
        except:
            print ('Houve um erro ao editar o arquivo')
        else:
            print (f'Informações de {nome} adicionadas com sucesso.')
            file.close()



