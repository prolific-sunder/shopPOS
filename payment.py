from typing import Protocol
from enum import Enum
#######
# PayType(Enum): Cash: 1, Card: 2, Phone: 3
######
class PayType(Enum):
  CASH = 1
  CARD = 2
  PHONE = 3
  TEST = 4                    #only added this for test cases
############
# A Protocol class Payable
# get_pay_type(self)
# set_pay_type(self, payment method: PayType)
#############
class Payable(Protocol):
  def get_pay_type(self):
    ...
  def set_pay_type(self, payment_method: PayType):
    ...
