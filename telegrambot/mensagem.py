import json
import requests
import time

# Informações do grupo, token, API
chat_id = -356717830
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

mensagem()



        




