from random import *
from flask import Flask, jsonify

app = Flask('__name__')

# Decorator para fazer a primeira rota. Decorator são funções já criadas para serem acopladas


@app.route('/api')
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
    final = jsonify({"lista": listaFinal})
    return final


def randomPar():
    paresPrincipais = ['EUR/USD', 'GBP/USD', 'EUR/GBP',
                       'USD/JPY', 'EUR/JPY', 'CAD/JPY', 'GBP/JPY', 'AUD/JPY']
    numberRandom = randint(0, 7)
    return paresPrincipais[numberRandom]


def hoursFormat(hor):
    if hor < 10:
        return (f"0{hor}")
    else:
        return hor


def minutesFormat(minu):
    if minu < 10:
        return (f"0{minu}")
    else:
        return minu




# para não ficar reiniciando o servidor, usaremos debug=True

app.run(debug=True)
