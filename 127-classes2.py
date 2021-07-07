class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada: # todo if já é True por padrão, não precisa colocar if self.ligada == True
            self.ligada = False
        else:
            self.ligada = True

    def aumentaCanal(self):
        if self.ligada:
            self.canal += 1
        else:
            print ('A TV está desligada')

    def diminuiCanal(self):
        if self.ligada:
            self.canal -= 1
        else:
            print ('A TV está desligada')


tv = Televisão()
print (tv.ligada)
tv.power()
print (tv.ligada)
tv.power()
print (tv.ligada)

print (f'Está no canal : {tv.canal}')
tv.aumentaCanal()
tv.aumentaCanal()
print (f'Está no canal : {tv.canal}')
tv.diminuiCanal()
print (f'Está no canal : {tv.canal}')


    