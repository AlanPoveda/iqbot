from random import *
from iqoptionapi.stable_api import IQ_Option
import sys
import time

#Fazendo login

API = IQ_Option('potatopn@gmail.com', '!4lanP0veda*')
API.connect()

#Troca de conta

API.change_balance('PRACTICE')

#Verificação de conexão

if API.check_connect():
    print("Você esta conectado com Sucesso")
else:
    print("Erro na conexão, verifique usuário ou senha")
    input('Clique enter para finalizar')
    sys.exit()


valorGasto = 5

pares = ["EURUSD-OTC", "EURGBP-OTC",'EURJPY-OTC','USDCHF-OTC','GBPUSD-OTC','AUDCAD-OTC']
numberRandom = randint(0,5)
par = pares[numberRandom]
valor = valorGasto
entrada ='put'
tempo = 1

gale = 0
erro = 0
acerto = 0
doji = 0





while True:
    status_compra, id = API.buy(valor, par, entrada, tempo)
    print("Status da compra: ", status_compra, id)
    print("Aguardando resultado...")

    while status_compra == False:
        numberRandom = randint(0,5)
        par = pares[numberRandom]
        status_compra, id = API.buy(valor, par, entrada, tempo)
    
    result = API.check_win_v3(id)

    if result < 0:
        valor = (valor * 1.15)*2
        erro += 1
        
        if erro > 2:
            numberRandom = randint(0,5)
            par = pares[numberRandom]

    elif result == 0:
        doji+=1
    else:
        acerto += 1
        numberRandom = randint(0,5)
        par = pares[numberRandom]

        valor = valorGasto
        

        erro = 0

    


