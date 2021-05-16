from random import *
from iqoptionapi.stable_api import IQ_Option

username = 'potatopn@gmail.com'
password = '!4lanP0veda*'
valor = 2
tempo = 1
conta = 'PRACTICE'


class Gale:

    def __init__(self, user, password, valor, tempo, conta):
        self.API = IQ_Option(user, password)
        self.id_compra = ''
        self.loss = 0
        self.win = 0
        self.value = valor
        self.entrada = 'put'
        self.time = tempo
        self.account = conta
        self.pares = ['EURUSD-OTC', 'AUDCAD-OTC', 'NZDUSD-OTC',
                      'USDCHF-OTC', 'GBPUSD-OTC', 'EURJPY-OTC']
        self.par = self.pares[self.RandomNumber()]

    # Conectando na conta. Retorna se foi feito com sucesso ou não
    def Connection(self):
        self.API.connect()
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
        compra_status, self.id_compra = self.API.buy_digital_spot(self.par, self.value, self.entrada, self.time)
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

    # Retorna se bateu a meta ou não
    def winResult(self):
        self.win += 1
        self.loss = 0
        if self.win == 10:
            return print("Meta batida ;D")
        self.par = self.pares[self.RandomNumber()]
        self.Compra()

    # Faz o gale e ainda entra novamente até acertar ou falhar
    def lossResult(self):
        self.loss += 1
        if self.loss == 3:
            return print("Hit :/")
        else:
            newValue = self.galeValue()
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
    def galeValue(self):
        newValue = self.value
        newValue = (newValue*1.15)*2
        return newValue

     # Verificar e retorna o valor do resultado da operação

    def resultVerification(self, id):
        self.API.check_win_digital_v2(self.id_compra)
        return self.API.check_win_v3(self.id_compra)


Alan = Gale(username, password, valor, tempo, conta)
Alan.Connection()
Alan.Compra()
