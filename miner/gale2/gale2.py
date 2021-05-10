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

    def __init__(self, user, password):
        self.API = IQ_Option(user, password)
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
    def Compra(self, valor, entrada, tempo):
        print('Make a buy...')
        initValue = valor
        loss = 0
        win = 0
        num = self.RandomNumber()
        par = self.pares[num]
        compra_status, id_compra = self.API.buy(valor, par, entrada, tempo)
        if compra_status == False:
            print('Buy Again')
            self.Compra(valor, entrada, tempo)
        else:
            print('waiting for the result of the order...')
            result = self.API.check_win_v3(id_compra)
            while result < 0:
                loss += 1
                valor = self.Gale(valor)
                self.API.buy(valor, par, entrada, tempo)
                if loss > 3:
                    return 'Loss'
                    break
            win += 1
            valor = initValue
            loss = 0
            num = self.RandomNumber()
            if win == 2:
                return 'Meta batida'
            self.Compra(valor, entrada, tempo)

    # Recebe o valor anterior e retorna com o novo valor
    def Gale(self, newValue):
        newValue = (newValue*1.15)*2
        return newValue

        


Alan = Gale(username, password)
Alan.Connection()
print(Alan.Compra(valor, entrada, tempo))
