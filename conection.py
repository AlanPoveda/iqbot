from iqoptionapi.stable_api import IQ_Option

import sys
from datetime import datetime, timedelta
from colorama import init, Fore, Back 
from time import time

init(autoreset=True)


API = IQ_Option('potatopn@gmail.com', '4lanP0veda*')
API.change_balance('PRACTICE') # PRACTICE / REAL


if API.check_connect():
    print("Conectado com sucesso")
else:
    print("Erro na selçao")
    input("Digite entter para sair")
    sys.exit()


def catalogar(par, dias, porcentagemCall, porcentagemPut, timeFrame ):
    data = []
    datas_testadas = []
    sair = False
    time_ = time()

    while sair == False:
        velas = API.get_candles(par,(timeFrame * 60), 1000, time_)
        velas.reverse()


        for x in velas:
            if datetime.fromtimestamp(x['from']).strftime('%Y-%m-%d') not in datas_testadas:
                datas_testadas.append(datetime.fromtimestamp(x['from']).strftime('%Y-%m-%d'))

            if len(datas_testadas)<= dias:
                x.update({ 'cor': 'verde' if x['open'] < x['close'] else 'vermelho' if x['open'] > x['close'] else 'doji' })
                data.append(x)

            else:
                sair == True
                break


        time_ = int(velas[-1]['from'] -1)



    analise = {}
    for velas in data:
        horario = datetime.fromtimestamp(velas['from']).strftime('%H-%M')
        if horario not in analise:
            analise.update({ horario: {'verde': o, 'vermelha': 0, 'doji': 0, '%': 0, 'dir': ''}})

        analise[horario][velas['cor']] += 1

        try:
            analise[horario]['%']= round(100*(analise[horario]['verde']/(analise[horario]['verde'] + analise[horario]['vermelho'] + analise[horario]['doji'])))
        except:
            pass


    for horario in analise:
        if analise[horario]['%'] > 50:
            analise[horario]['dir'] = 'CALL '
        if analise[horario]['%'] < 50:
            analise[horario]['dir'],analise[horario]["%"] = 'PUT ', (100 - analise[horario]['%'])

    return analise


print('\n\n Qual time frame esta querendo catalogar?,', end='')
timeFrame = int(input())


print("\nQuantos dias para analisar?", end="")
dias = int(input())

print('\nQual é a porcentágem minima?', end='')
porcentagem = int(input())

print('\nTestar com quantos Martingales: ', end = '')
martingale = input()

porcentagemCall = abs(porcentagem)
porcentagemPut = abs(100 - porcentagem)

#Aqui para ver o par moéda, digital ou binário
P = API.get_call_open_time()

print('\n\n\')

catalogacao = {}

for par in P['digital']: #Esta vendo os pares Digitais, podem ser binários
    if P['digital'][par]['open'] == True:
        timer = int(timer())

        print(Fore.GREEN + '+' + Fore.RESET + 'CATALOGANDO' + par + '..', end='')

        catalogacao.update({ par: cataloga(par,dias, porcentagemCall, porcentagemPut, timeFrame)})

        if martingale.strip() != '':
            for horario in sorted(catalogacao[par]):

