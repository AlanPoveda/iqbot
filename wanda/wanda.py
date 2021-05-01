from random import *
from flask import Flask, request, jsonify

app = Flask('__name__')

# Decorator para fazer a primeira rota. Decorator são funções já criadas para serem acopladas

# Função faz a parte lógica, e retorna um json com a lista completa
@app.route('/api', methods=['GET'])
def api():
    if request.method == 'GET':
        lista = jsonify({"lista": makeList()})
        return lista
    


def makeList():
    listaFinal = []
    cont = 0
    horas = 0
    minutos = 0
    for x in range(60):
        listaFinal.append(
            f"{randomPar()} -> {hoursFormat(horas)}:{minutesFormat(minutos)}")
        minutos += 15
        if minutos > 45:
            horas += 1
            minutos = 0
        cont += 1
    
    return listaFinal

# A função retorna o valor da moeda que será negociado
def randomPar():
    paresPrincipais = ['EUR/USD', 'GBP/USD', 'EUR/GBP',
                       'USD/JPY', 'EUR/JPY', 'CAD/JPY', 'GBP/JPY', 'AUD/JPY']
    numberRandom = randint(0, 7)
    return paresPrincipais[numberRandom]

# A função recebe horas, e retorna a hora no formato correto
def hoursFormat(hor):
    if hor < 10:
        return (f"0{hor}")
    else:
        return hor

# A função recebe os minutos e retorna os minutos no formato correto
def minutesFormat(minu):
    if minu < 10:
        return (f"0{minu}")
    else:
        return minu




# para não ficar reiniciando o servidor, usaremos debug=True

app.run(debug=True)
