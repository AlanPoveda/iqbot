import json
import requests
import time

# Informações do grupo, token, API
#chat_id = -356717830 #chat Grupo
chat_id = 378724848
token= '1731762118:AAEBEsvGvkc2JXUYVJJOO9JnmI4IfqdYBW4'
url_base = f'https://api.telegram.org/bot{token}/'
resposta = requests.get("http://127.0.0.1:5000/api")
lista = resposta.json()

def mensagem():
    # Formatação da lista que esta sendo gerada
    formatacao = ''
    for itens in lista['lista']:
        formatacao += f"{itens} PUT 🔻 \n"

    # Enviando para API do telegram
    link_de_envio = f"{url_base}sendMessage?chat_id={chat_id}&text={formatacao}"
    requests.get(link_de_envio)
    return "Enviado com sucesso"

print(mensagem())


""" *:gem:SINAIS VIP:gem:*

TODOS OS SINAIS SÃO PARA PUT :arrow_down: 
TEMPO DA VELA M5⏱
TEMPO DE OPERAÇÃO 5M⏱
LISTA DE ATÉ 2 GALE:chart_with_upwards_trend:

⚜OPERACIONAL DA WANDA⚜
 
SEGUNDA A SEXTA 
00H ATE AS 14H45⏱"""


        




