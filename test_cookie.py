import pytest
from dessert import DessertItem, Cookie

###############################
# Default value test cases
###############################

def test_cookie_default():
  cookie = Cookie()
  assert cookie.name == ""
  assert abs(cookie.cookie_quantity - 0) <= 0
  assert cookie.price_per_dozen == pytest.approx(0.0, abs = 10e-3)

##########################3
# Nominal value test cases
###########################

def test_cookie():
  cookie = Cookie("Snickerdoodle", 1, 9.00)
  assert cookie.name == "Snickerdoodle"
  assert abs(cookie.cookie_quantity - 1) <= 0
  assert abs(cookie.price_per_dozen - 9.00) <= 0.001

###################################
# Modify attributes test cases
###################################

def test_cookie():
  cookie = Cookie()
  cookie.name = "Snickerdoodle"
  assert cookie.name == "Snickerdoodle"
  cookie.cookie_quantity = 1
  assert abs(cookie.cookie_quantity - 1) <= 0
  cookie.price_per_dozen = 9.00
  assert abs(cookie.price_per_dozen - 9.00) <= 0.001

###################################
# Calculate cost test cases
###################################

def test_cookie_cost():
  cookie = Cookie("Snickerdoodle", 1, 9.00)
  assert cookie.calculate_cost() == pytest.approx((1/12) * 9, abs=1e-2)

##########################3
# Packaging test case
###########################

def test_cookie_pack():
  cookie = Cookie("Sugar", 3, 10)
  assert cookie.packaging == "Box"

##########################
# Combining
##########################

def two_cookies():
  first = Cookie("Sugar", 3, 10)
  second = Cookie("Sugar", 2, 10)
  assert first.can_combine(second) == True

def one_cookie():
  first = Cookie("Sugar", 3, 10)
  second = Candy("Sugar", 2, 10)
  assert first.can_combine(second) == False

def combine():
  first = Cookie("Sugar", 3, 10)
  second = Cookie("Sugar", 2, 10)
  assert first.combine(second) == Cookie("Sugar", 5, 10)

def fail():
  first = Cookie("Sugar", 3, 10)
  second = Candy("Sugar", 2, 10)
  assert first.combine(second) == (Cookie("Sugar", 5, 10))

if __name__ == "__main__":
  pytest.main([__file__])
