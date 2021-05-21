# Criação de despertador para poder upar e fazer de forma automzatizada o envio de mensangens

import mensagem
import time
import datetime


def Horas():
  while True:
    timevalue = datetime.datetime.now()
    now = timevalue.strftime('%H:%M:%S')
    horas = timevalue.strftime('%H')
    print(horas)
    print(now)
    while horas >= '19' and now < '20:00:02':
      time.sleep(1)
      if now >= '20:00:00':
        ExecMessage()
        break
  else:
    time.sleep(10)


def ExecMessage():
  return print(mensagem.Mensagem())
