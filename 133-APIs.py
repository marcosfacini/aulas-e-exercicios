""" Hoje em dia é muito comum que diferentes aplicações consumam dados pela internet, muitas vezes dados providenciados por terceiros. 
Por exemplo, um aplicativo de entrega de alimentos pode usar dados de geolocalização do Google 
para localizar restaurantes próximos ao usuário e exibir a rota percorrida pelo entregador.
Ou um widget de clima no seu celular que pega as informações de um site de clima/tempo
Como as aplicações podem rodar em diferentes plataformas (Windows, Android, MacOS, iOS, um navegador de internet...), 
é importante estabelecer uma linguagem comum para que todos consigam consumir esses dados.
Essa "linguagem comum" é o que chamamos de API: Application Programming Interface. 
A organização que disponibiliza os dados estabelece algumas "regrinhas" para fazermos requisições, 
e em contrapartida ela garante que os recursos fornecidos também seguirão certos padrões, facilitando a vida dos programadores.
Portanto, quando decidimos utilizar uma API, a primeira coisa que precisamos fazer é estudar sua documentação """

""" URI base
Várias APIs fornecem um "endereço base". 
Todas as suas requisições incluirão esse endereço, e ao final dele nós colocamos detalhes específicos para cada um dos recursos disponíveis.
Por exemplo, na AlphaVantage (https://www.alphavantage.co/), uma API de dados de bolsas de valores e criptomoedas, a URI base é:
https://www.alphavantage.co/query?
Após a interrogação nós colocaremos os campos para nossa consulta. Por exemplo, para fazer uma consulta sem autenticação para valores da IBM, de 5 em 5 minutos, o endereço completo fica:
https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo """

""" Outro formato bastante comum é o de "subdiretórios".
Um exemplo é a PokéAPI. A URI base é:
https://pokeapi.co/api/v2/
Para procurar por pokémons, adicionamos pokemon/. Em seguida, podemos colocar números (índices) ou nomes de Pokémon, como:
https://pokeapi.co/api/v2/pokemon/ditto/
https://pokeapi.co/api/v2/pokemon/25
Se ao invés de pokémons estivéssemos interessados em tipos de pokémon, usaríamos types/ e o nome ou índice do tipo desejado:
https://pokeapi.co/api/v2/type/ghost """

# As APIs são meios de nos conectarmos a recursos na internet. 
# normalmente uma API vai ultilizar dados em .json, .xml ou .csv
# o python contem bibliotecas especificas para manipular cada um desses tipos de arquivo

""" Descobrindo APIs: tem boas ideias e gostaria de saber se existe uma boa API para ajudar? 
Confira alguns bons repositórios de API organizados por categoria:

https://github.com/n0shake/public-apis

https://github.com/public-apis/public-apis

https://any-api.com/

Sites de governos costumam ter uma grande riqueza de dados também. 
Segue abaixo algumas sugestões (oficiais ou mantidas por voluntários) com dados do Brasil como um todo. 
Experimente buscar por bases de dados de sua cidade ou estado!

http://www.transparencia.gov.br/swagger-ui.html

http://www.dados.gov.br/

https://brasil.io/home/ """


# exemplo de API de conversão de moeda 
# documentação da API: https://www.exchangerate-api.com/docs/free-exchange-rate-api

#importar biblioteca requests
import requests

url = 'https://api.exchangerate-api.com/v6/latest'

# metodo get() pega as informações da url informada
requisição = requests.get(url)

# metodo status_code() verifica o status da requisição feita
# retorna 404 quando  not found
# retorna 200 se estiver tudo ok
print (requisição.status_code)

# variavel dados vai receber a requisição em formato .json que se assemelha muito ao dicionario do python
dados = requisição.json()
print (dados)

# usuario informa o valor a ser convertido para dolar que é a moeda base chamado de base_code no arquivo .json
valor_reais = float (input ('Informe o valor em R$ a ser convertido:\n '))

# variavel cotação recebe o value da key BRL dentro da key rates
cotação = dados['rates']['BRL']

# variavel resultado faz a conversão
resultado = valor_reais / cotação

print (f'R$ {valor_reais:.2f} convertido em dólar vale: USD {resultado:.2f}')
