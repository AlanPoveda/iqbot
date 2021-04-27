import json
import requests
import time
from threading import Thread, Lock


class HermesBot:
    def __init__(self):
        token = '1731762118:AAEBEsvGvkc2JXUYVJJOO9JnmI4IfqdYBW4'
        self.url_base = f'https://api.telegram.org/bot{token}/'
        # Iniciar bot

    def iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_mensagens(update_id)
            mensagens = atualizacao['result']
            if mensagens:
                for mensagem in mensagens:
                    update_id = mensagem['update_id']
                    chat_id = mensagem['message']['from']['id']
                    # Criar a resposta
                    resposta = self.criar_resposta()
                    # Responder a pessoa
                    self.responder(resposta, chat_id)

    # Obter Mensagens, assim ele fala com você

    def obter_mensagens(self, update_id):
        # Para ele verificar a cada 100 segundos
        link_requisicao = f"{self.url_base}getUpdates?timeout=100"
        if update_id:
            # Assim ele vai pegar a ultima mensagem
            link_requisicao = f"{link_requisicao}&offset={update_id + 1}"
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta

    def criar_resposta(self):
        return "Hello world"
    # Responder

    def responder(self, resposta, chat_id):
        # Enviar
        link_de_envio = f"{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}"
        # Fazer a requisição
        requests.get(link_de_envio)


bot = HermesBot()

bot.iniciar()
