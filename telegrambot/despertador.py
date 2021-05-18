# Criação de despertador para poder upar e fazer de forma automzatizada o envio de mensangens

import mensagem
import time
import datetime


while True:
  timevalue = datetime.datetime.now()
  now = timevalue.strftime('%H:%M:%S')
  horas = timevalue.strftime('%H')
  print(horas)
  print(now)
  if horas > '19':
    while horas > '19':
      time.sleep(1)
      if now >= '20:00:00':
        print(mensagem.Mensagem())
        break
  else:
    time.sleep(10)


