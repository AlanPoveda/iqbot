from iqoptionapi.stable_api import IQ_Option
import sys
import time

#Fazendo login na IQ
API = IQ_Option('potatopn@gmail.com', '!4lanP0veda*')
API.connect()

#Trocando a conta, pode ser para 'REAL'/'PRACTICE'
API.change_balance("PRACTICE")

#Verificando conexão
if API.check_connect():
    print("Você esta conectado com sucesso!")
else:
    print("Ocorreu um erro na conexão")
    input('Clique enter para finaliza')
    sys.exit()

#Fazendo a compra do ativo

#Compra na digital
#buy_digital_spot (par, valor, tipo_de_ordem, time_frame)
status_digital, id_digital = API.buy_digital_spot('EURUSD', 2, 'put', 1)

print("Status da compra no digital: ", status_digital, id_digital)

#Compra na compra binária
#buy(valor, par, tipo_de_ordem, time_frame)
status_binaria, id_binaria = API.buy(2, 'EURUSD', 'put', 1)

print("\nStatus compra da binária: ", status_binaria, id_binaria)


# Para fazer a venda das operações
time.sleep(3)

print('Vendnedo digital: ', end='')

#---------------------------------------------------------------------------------------------------
#Para vender a ordem no digital
status = API.close_digital_option(id_digital)
if status == True:
    print('Operação vendida com sucesso')
else:
    print('Erro na execução da venda')

print(status)
print('\n\n\n\')

#Status de resultado da binária

print('Vendendo binária', end='')
status = API.sell_option(id_binaria)

if 'error' in status[msg]:
    print('Ocorreu um erro com a operação')
else:
    print("Operação bem sucedida na binária")

print(status)


