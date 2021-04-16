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

#API.buy(2, 'EURUSD', 'put', 1) binário

while True:
    compra_status, id_compra = API.buy_digital_spot("EURUSD", 1, 'put', 5)
    print("Status da compra: ", compra_status, id_compra)
    #Tempo para executar novamente, 5 min
    time.sleep(300)