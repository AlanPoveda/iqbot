from random import *
from iqoptionapi.stable_api import IQ_Option

username = input(str('Username: '))
password = input(str('Padssword: '))
valor = 10
tempo = 1
conta = 'PRACTICE'


class Gale:

    def __init__(self, user, password, valor, tempo, conta):
        self.API = IQ_Option(user, password)
        self.id_compra = ''
        self.loss = 0
        self.galeloss = 0
        self.win = 0
        self.value = valor
        self.gale = valor
        self.entrada = 'put'
        self.time = tempo
        self.account = conta
        self.pares = ['NZDUSD-OTC', 'AUDCAD-OTC', 'EURJPY-OTC']
        self.par = self.pares[self.RandomNumber()]

    # Conectando na conta. Retorna se foi feito com sucesso ou não
    def Connection(self):
        self.API.connect()
        self.Account()
        if self.API.connect():
            return print('Successfully connected :D')
        else:
            return print('Conection Error D:')

    # Retorna tipo de conta, se é real ou de pratica
    def Account(self):
        return self.API.change_balance(self.account)

    # Gerando um número random
    def RandomNumber(self):
        numberRandom = randint(0, len(self.pares)-1)
        return numberRandom

    # Recebe valor, entrada, tempo
    def Compra(self):
        print('Make a buy...')
        compra_status, self.id_compra = self.API.buy(
            self.value, self.par, self.entrada, self.time)
        if compra_status == False:
            print('Buy Again')
            self.par = self.pares[self.RandomNumber()]
            self.Compra()
        else:
            print('waiting for the result of the order...')
            result = self.resultVerification(self.id_compra)
            if result > 0:
                self.winResult()
            elif result == 0:
                self.Compra()
            else:
                self.lossResult()

    # Retorna se bateu a meta
    def winResult(self):
        self.win += 1
        self.galeloss = 0
        self.gale = self.value
        self.loss = 0
        if self.win == 100:
            return print("Goal hit ;D")
        self.par = self.pares[self.RandomNumber()]
        self.Compra()

    # Retorna se deu loss ou hit
    def lossResult(self):
        self.loss += 1
        if self.loss == 3:
            print("Hit :/")
            return self.Compra()
        else:
            newValue = self.galeValue(self.gale)
            compra_status, self.id_compra = self.API.buy(
                newValue, self.par, self.entrada, self.time)
            newResult = self.resultVerification(self.id_compra)
            if newResult < 0:
                self.lossResult()
            elif newResult == 0:
                self.API.buy(newValue, self.par, self.entrada, self.time)
            else:
                newValue = self.value
                self.winResult()

    # Retorna o novo valor, fazendo o Maringale
    def galeValue(self, galeValue):
        self.galeloss+=1
        if self.galeloss == 1:
            galeValue = galeValue*3
        elif self.galeloss == 2:
            galeValue = galeValue*5
        
        self.gale = galeValue
        return galeValue

     # Verificar e retorna o valor do resultado da operação

    def resultVerification(self, id):
        return self.API.check_win_v3(self.id_compra)


Alan = Gale(username, password, valor, tempo, conta)
Alan.Connection()
Alan.Compra()
