# Crie um código em Python que teste se o site pudim (www.pudim.com.br) está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com.br')
except:
    print ('O site Pudim não está acessível no momento')
else:
    print ('Consegui acessar o site do Google com sucesso.')
    # print (site.read()) essa função consegue printar o conteudo HTML do site