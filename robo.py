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

        self.dados_operacao = {
            'pares' : ["EURUSD-OTC", "EURGBP-OTC",'EURJPY-OTC','USDCHF-OTC','GBPUSD-OTC','AUDCAD-OTC'],
            'valor' : self.valor,
            'entrada': self.entrada,

        }
    
    # recebe a conexão, retorna mensagem se conecta ou não
    def conexao(self):
        self.API.connect()
        if self.API.check_connect():
            print("Você está conectado :D")
            tipo_conta() 
        else:
            return "Ocorreu um erro na conexão"

    # retorna o balanço da conta
    def tipo_conta(self):
        self.API.change_balance(self.conta)
        compra()

    # Retorna status da compra e id da compra
    def compra(self, valor, par, entrada, tempo):
        compra_status, id_compra = self.API.buy(valor, par, entrada, tempo)
        while compra_status == False:
            
        resultado(id_compra)
        return compra_status, id_compra


    # Retorna o resultado da compra
    def resultado(self, id):
        result = self.API.check_win_v3(id)
        return result

    



    



robo = Robo(login, password)

print(robo.Conexao())







