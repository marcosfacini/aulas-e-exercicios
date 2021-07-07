from datetime import date, time, datetime, timedelta

# data atual no padrão americano
""" data_atual = date.today()
print (data_atual) """

# converter data para string para poder formata-la para o padrao brasileiro
""" data_atual = date.today()
print (data_atual.strftime('%d/%m/%y')) """

# consultar as diretivas do modulo datetime na documentação para saber as alterações que podem ser feitas
# por exemplo, se colocar o y de year/ano em maisculo, retorna o valor do ano com 4 digitos ao inves de 2
# e pode substituir as barras que separam por qualquer outra coisa que for conveniente
""" data_atual = date.today()
print (data_atual.strftime('%d-%m-%Y')) """

# trabalhando com horario usando a função time
""" horario = time(hour=14, minute=35, second=46)
print (horario) """

# é possivel converter o horario para string para poder formata-lo
""" horario = time(hour=14, minute=35, second=46)
print (horario.strftime('%H Horas %M Minutos %S Segundos')) """

# função datetime dentro do modulo datetime já permite trabalhar tanto com a data, quanto com o horario
""" data = datetime.now()
print (data) """

# pode fazer as formatações necessarias usando tambem o metodo strftime()
""" data = datetime.now()
print (data.strftime('%H Horas %M Minutos %S Segundos %d-%m-%Y'))
print (data.strftime('%c'))

# trazendo so uma informação do datetime
print (data.year) # só o ano

# só o dia da semana
# porem ele retorna em um indice que começa na segunda valendo 0
print (data.weekday()) 

# jeito de "traduzir" o dia da semana
tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
print (tupla[data.weekday()]) """

# criando uma data no datetime
""" data_craiada = datetime(1992, 11, 18, 8, 35, 22)
print (data_craiada) """

# convertendo uma string em datetime
data_string = '18/11/1992 12:34:15'
data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
print (data_convertida)

# subtraindo data com a função timedelta()
sub_data = data_convertida - timedelta(days=365, hours=2, minutes=4)
print (sub_data)