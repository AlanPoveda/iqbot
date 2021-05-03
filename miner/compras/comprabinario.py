from random import *
from iqoptionapi.stable_api import IQ_Option
import sys
import time

# Fazendo login

API = IQ_Option('potatopn@gmail.com', '!4lanP0veda*')
API.connect()

# Troca de conta

API.change_balance('PRACTICE')

# Verificação de conexão

if API.check_connect():
    print("Você esta conectado com Sucesso")
else:
    print("Erro na conexão, verifique usuário ou senha")
    input('Clique enter para finalizar')
    sys.exit()

# Fazendo a compra

investimento = 5
gale = 4

#pares = ["EURUSD-OTC","GBPUSD-OTC", "EURGBP-OTC",'USDJPY-OTC', 'EURJPY-OTC','CADJPY-OTC','GBPJPY-OTC','AUDJPY-OTC']
pares = ["EURUSD", "EURGBP", 'EURJPY', 'USDCHF', 'GBPUSD', 'AUDCAD']
numberRandom = randint(0, 5)
valor = investimento
entrada = 'put'
tempo = 5

banca = API.get_balance()
metaPorcentagem = 20
meta = banca*((100/metaPorcentagem)+1)



quantidadeentradas = 0
acerto = 0
erroCont = 0
erro = 0
doji = 0

par = pares[numberRandom]

acertividade = 0




while banca < meta:            
    #Informação da banca
    
    print("O par que esta sendo comprado: ", par)

    # Compra
    compra_status, id = API.buy(valor, par, entrada, tempo)

    print("Status da compra: ", compra_status, id)
    
    while compra_status == False:
        numberRandom = randint(0, 5)
        par = pares[numberRandom]
        compra_status, id = API.buy_digital_spot(par, valor, entrada, tempo)
        if compra_status == True:
            print("O par que esta sendo comprado: ", par)
            print("Status da compra: ", compra_status, id)
            break
    print("Aguardando resultado...")
    result = API.check_win_v3(id)

    if result > 0:
        acerto += 1
        numberRandom = randint(0, 5)
        par = pares[numberRandom]

        valor = investimento
        acertividade = (100*acerto)/(acerto+erroCont)
        erro = 0
    elif result == 0:
        doji += 0
    elif result < 0:
        valor = (valor * 1.15)*2
        erro += 1
        if erro > gale:
            erroCont += 1
            numberRandom = randint(0, 5)
            par = pares[numberRandom]

            valor = investimento
            erro = 0
            acertividade = (100*acerto)/(acerto+erroCont)

    quantidadeentradas += 1

    print('Total de entradas :', quantidadeentradas)
    print('Acertos: ', acerto)
    print('Erros: ', erroCont)
    print('Porcentagem de acertividade: ', acertividade, '%')    
    

   
