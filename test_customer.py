import pytest
from dessertshop import DessertItem, Customer

#################
#CUSTOMER
#################

def test_name():
  customer = Customer("Jane")
  assert customer.customer_name == "Jane"

def test_order():
  customer = Customer("Jane")
  assert customer.order_history == []

def test_id():
  customer = Customer("Jane")
  customer2 = Customer("Joe")
  assert customer.customer_id != customer2.customer_id

if __name__ == "__main__":
  pytest.main([__file__])
