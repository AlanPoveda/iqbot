from random import *
from iqoptionapi.stable_api import IQ_Option
import sys
import time

username = 'potatopn@gmail.com'
password = '!4lanP0veda*'
valor = 2
tempo = 1
entrada = 'put'


class Gale:

    def __init__(self, user, password, valor):
        self.API = IQ_Option(user, password)
        self.id_compra = ''
        self.loss = 0
        self.win = 0
        self.value = valor
        self.account = 'PRACTICE'
        self.pares = ['EURUSD', 'EURGBP',
                      'EURJPY', 'USDCHF', 'GBPUSD', 'AUDCAD']

    # Conectando na conta. Retorna se foi feito com sucesso ou não
    def Connection(self):
        self.API.connect()
        if self.API.connect():
            return 'Successfully connected :D'
        else:
            return 'Conection Error D:'

    # Retorna tipo de conta, se é real ou de pratica
    def Account(self):
        return self.API.change_balance(self.account)

    # Gerando um número random
    def RandomNumber(self):
        numberRandom = randint(0, len(self.pares)-1)
        return numberRandom

    # Recebe valor, entrada, tempo
    # arrumar
    def Compra(self, entrada, tempo):
        print('Make a buy...')
        initValue = self.value
        num = self.RandomNumber()
        par = self.pares[num]
        compra_status, self.id_compra = self.API.buy(self.value, par, entrada, tempo)
        if compra_status == False:
            print('Buy Again')
            self.Compra(entrada, tempo)
        else:
            print('waiting for the result of the order...')
            result = self.resultVerification()
            if result > 0:
                self.win += 1
                self.loss = 0
                self.value = initValue
                if self.win ==2:
                    return print('Meta batida')
                self.Compra(entrada, tempo)
            elif result < 0:
                self.loss += 1
                if self.loss == 3:
                    return print('Hit')
                self.value = self.Gale(initValue)
                self.Compra(entrada, tempo)
                self.value = initValue




                
                

    # Verificar resultado
    def resultVerification(self):
        return self.API.check_win_v3(self.id_compra)

    # Recebe o valor anterior e retorna com o novo valor
    def Gale(self, newValue):
        newValue = (newValue*1.15)*2

        return newValue

        


Alan = Gale(username, password, valor)
Alan.Connection()
Alan.Compra(entrada, tempo)
