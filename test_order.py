import pytest
from dessert import Order
from payment import PayType

###
#TESTS FOR PAYMENT
###
def test_order_type1():
  req = Order()
  assert req.get_pay_type() == PayType.CASH
#####
# Set the meal type to MealType(2), i.e. MealType.LUNCH
# Change to BREAKFAST
####
def test_order_type2():
  req = Order()
  req.set_pay_type(PayType(2))
  assert req.get_pay_type() == PayType.CARD
  req.set_pay_type(PayType.CASH)
  assert req.get_pay_type() == PayType.CASH
#####
# Set the meal type to MealType(3), i.e. MealType.DINNER
####
def test_order_type2():
  req = Order()
  req.set_pay_type(PayType(3))
  assert req.get_pay_type() == PayType.PHONE
#############
# Set an invaild value MealType(4)
############
def test_set_invaild():
  req = Order()
  with pytest.raises(ValueError):
    req.set_pay_type(PayType(4))
  with pytest.raises(ValueError):
    req.set_pay_type(PayType(5))
#######
# Get a invaild MealType
##########
def test_get_invaild():
  req = Order()
  req.pay_type = PayType(4)
  with pytest.raises(ValueError):
    req.get_pay_type()

####
#Test sort
####
def test_sort():
  req = Order()
  req.add(2)
  req.add(1.5)
  req.add(4)
  req.sort_order()
  assert req.order == [1.5, 2, 4]

if __name__ == "__main__":
  pytest.main([__file__])
