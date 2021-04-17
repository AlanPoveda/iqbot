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



ativo = "EURUSD-OTC"
valor = 1
entrada ='put'
tempo =5

while True:
    compra_status, id_compra = API.buy(1, 'EURUSD-OTC', 'put', 5)
    #compra_status, id_compra = API.buy_digital_spot(ativo, valor, entrada, tempo )
    print("Status da compra: ", compra_status, id_compra)
    #Tempo para executar novamente, 5 min
    time.sleep(300)