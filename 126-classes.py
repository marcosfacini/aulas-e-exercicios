# classe é uma maneira de agrupar e organizar um grupo de metodos
# toda def é um método que recebe parenteses "()"" no final e pode receber parametros dentro desses parenteses
# se um metodo retorna um valor ele é chamada de função
# ou seja, toda função é um metodo, mas nem todo método é uma função

# metodo __init__ inicializa a classe
""" class Calculadora:
    def __init__(self, a, b):
        self.parametro1 = a
        self.parametro2 = b

    def soma(self):
        return self.parametro1 + self.parametro2

    def subtração(self):
        return self.parametro1 - self.parametro2

    def multiplicação(self):
        return self.parametro1 * self.parametro2

    def divisão(self):
        return self.parametro1 / self.parametro2

# desse forma os parametros só são passados uma vez
calculo = Calculadora(10, 2)
print (calculo.soma())
print (calculo.subtração())
print (calculo.multiplicação())
print (calculo.divisão()) """

# é possível acessar um parametro especeifico
# print (calculo.parametro2)

# outro jeito sem passar o self dentro do __init__
# coloca-se o pass dentro do __init__ para ele não fazer nada e passar direto
# ou simplismente não se usa o __init__ nesse caso, que funcionaria do mesmo jeito
# desse jeito todas as funções precisaram receber os seus parametros
class Calculadora:
    def __init__(self):
        pass
        
    def soma(self, parametro1, parametro2):
        return parametro1 + parametro2

    def subtração(self, parametro1, parametro2):
        return parametro1 - parametro2

    def multiplicação(self, parametro1, parametro2):
        return parametro1 * parametro2

    def divisão(self, parametro1, parametro2):
        return parametro1 / parametro2

calculo = Calculadora()
print (calculo.soma(10, 2))
print (calculo.subtração(10, 2))
print (calculo.multiplicação(10, 2))
print (calculo.divisão(10, 2))
    

