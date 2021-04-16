from iqoptionapi.stable_api import IQ_Option
import logging

#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
I_want_money=IQ_Option("potatopn@gmail.com","!4lanP0veda*")
check, reason=I_want_money.connect()#connect to iqoption
MODE ="REAL"
balance = I_want_money.get_balance()
print(check, reason, balance)