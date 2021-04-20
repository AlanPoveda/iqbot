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

#Fazendo a compra

investimento = 10

pares = ["EURUSD","GBPUSD", "EURGBP",'USDJPY', 'EURJPY','CADJPY','GBPJPY','AUDJPY']
#pares = ["EURUSD", "EURGBP",'EURJPY','USDCHF','GBPUSD']
numberRandom = randint(0,7)
valor = investimento
entrada ='put'
tempo = 1



banca = API.get_balance()
metaPorcentagem = 2
meta = banca*(100/metaPorcentagem)


quantidadeentradas = 0 
acerto = 0 
erroCont = 0
erro = 0
doji = 0

par = pares[numberRandom]

acertividade = 0

#compra_status, id_compra = API.buy_digital_spot(pares, valor, entrada, tempo )

while True:
    print("O par que esta sendo comprado: ", par)

    #Compra
    #compra_status, id = API.buy(valor, par, entrada, tempo)
    compra_status, id = API.buy_digital_spot(par, valor, entrada, tempo )
    
    print("Status da compra: ", compra_status, id)
    print("Aguardando resultado...")
    while compra_status == False:
        numberRandom = randint(0,7)
        par = pares[numberRandom]
        compra_status, id = API.buy_digital_spot(par, valor, entrada, tempo )
        if compra_status == True:
            break
    #result = API.check_win_v3(id)
    
    while True:
        check, win = API.check_win_digital_v2(id)    
        if check==True:
            break
 
   
    if win<0:
        valor = (valor * 1.05)*2
        erro += 1
        if erro > 4:
            erroCont += 1
            numberRandom = randint(0,7)
            par = pares[numberRandom]
            
            valor = investimento
            erro = 0
            acertividade = (100*acerto)/(acerto+erroCont)
    else:
        acerto += 1
        numberRandom = randint(0,7)
        par = pares[numberRandom]

        valor = investimento
        acertividade = (100*acerto)/(acerto+erroCont)
        erro = 0

    quantidadeentradas += 1
    


    
    
    print('Total de entradas :', quantidadeentradas)
    print('Acertos: ', acerto)
    print('Erros: ', erroCont)
    print('Porcentagem de acertividade: ', acertividade, '%')
    if banca >= meta:
        break
    
    
    
    
