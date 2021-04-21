from flask import Flask

app = Flask('teste')

@app.route('/ola')
def ola():
    return "Olá mundo"



