from random import *
from iqoptionapi.stable_api import IQ_Option
import sys
import time

login = 'potatopn@gmail.com'
password = '!4lanP0veda*'


class Robo:

    # recebe login e senha para logar API
    def __init__(self, login, senha):
        self.API = IQ_Option(login, senha)
        self.conta = 'PRACTICE'
        self.valor = 1
        self.entrada = "put"

        self.dados_operacao = {
            'pares' : ["EURUSD-OTC", "EURGBP-OTC",'EURJPY-OTC','USDCHF-OTC','GBPUSD-OTC','AUDCAD-OTC'],
            'valor' : self.valor,
            'entrada': self.entrada,

        }
    
    # recebe a conexão, retorna mensagem se conecta ou não
    def Conexao(self):
        self.API.connect()
        if self.API.check_connect():
            return "Você está conectado :D"
        else:
            return "Ocorreu um erro na conexão"

    # retorna o balanço da conta
    def Tipo_conta(self):
        return self.API.change_balance(self.conta)

    # Retorna status da compra e id da compra
    def Compra(self):
        return compra_status, id_compra = self.API.buy(self.valor,)


    



robo = Robo(login, password)

print(robo.Conexao())







