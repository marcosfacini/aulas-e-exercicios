larg = float (input ('Qual é a largura da parede?: '))
alt = float (input ('Qual é a altura da parede?: '))
m2 = larg * alt
tinta = m2 / 2

print ('Sua parede tem a dimensão de {:.2f}x{:.2f} e a sua área é de {:.2f}m²'.format(larg, alt, m2))

print ('Para pintar essa parede você precisará de {:.2f} litros de tinta.'.format(tinta))

# a cada 2 metros quadrados 1 litro de tinta