# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.Depois mostre:
# Os 5 primeiros times.
# Os últimos 4 colocados.
# Times em ordem alfabética. 
# Em que posição está o time da Chapecoense. - 17º

times = ('Palmeiras', 'Corintians', 'Santos', 'São Paulo', 'Flamengo', 'Botafogo', 'Vasco', 'Fluminense', 'Curitiba', 'Goiais', 
'Atlético', 'Internacional', 'Gremio', 'Cruzeiro', 'Bahia', 'Sport', 'Chapecoense', 'Portuguesa', 'Ibis', 'Barcelona')

print (f'Os 5 primeiros colocados são: {times[:5]}')
print (f'Os 4 ultimos colocados são: {times[16:]} ')
print (f'Ordem alfabética: {sorted(times)}')
print (f'O time da Chapecoense está na {times.index("Chapecoense")+1}º posição.')