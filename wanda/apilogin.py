from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import os
from random import *


app = Flask(__name__)

# Rota para fazer o login, e retorna a api
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return api()

# Uma validação simples para fazer o login
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'test.123' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

#lugar para fazer logout
@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()

#Rota da api
@app.route('/api')
def api():
    # if request.method == 'GET':
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


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, port=4000)
