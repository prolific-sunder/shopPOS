import pytest
from dessert import DessertItem, Candy

###############################
# Default value test cases
###############################

def test_candy_default():
  candy = Candy()
  assert candy.name == ""
  assert abs(candy.candy_weight - 0.0) <= 0.01
  assert candy.price_per_pound == pytest.approx(0.0, abs = 10e-3)

##########################3
# Nominal value test cases
###########################

def test_candy():
  candy = Candy("gummy bears", 3, 12.00)
  assert candy.name == "gummy bears"
  assert abs(candy.candy_weight - 3.0) < 0.001
  assert abs(candy.price_per_pound - 12.00) < 0.001

###################################
# Modify attributes test cases
###################################

def test_candy_modify():
  candy = Candy()
  candy.name = "gummy bears"
  assert candy.name == "gummy bears"
  candy.weight = 3.0
  assert abs(candy.weight - 3.0) < 0.01
  candy.price_per_pound = 12.00
  assert abs(candy.price_per_pound - 12.00) < 0.01

###################################
# Calculate cost test cases
###################################

def test_candy_cost():
  candy = Candy("gummy bears", 3, 12.00)
  assert candy.calculate_cost() == pytest.approx(3.0 *12.00, abs=1e-2)

##########################3
# Packaging test case
###########################

def test_candy_pack():
  candy = Candy("Gummy Bear", 3, 12)
  assert candy.packaging == "Bag"

##########################
# Combining
##########################

def two_candy():
  first = Candy("Gummy Bear", 3, 12)
  second = Candy("Gummy Bear", 4, 12)
  assert first.can_combine(second) == True

def one_candy():
  first = Candy("Gummy Bear", 3, 12)
  second = Cookie("Gummy Bear", 4, 12)
  assert first.can_combine(second) == False

def combine():
  first = Candy("Gummy Bear", 3, 12)
  second = Candy("Gummy Bear", 4, 12)
  assert first.combine(second) == Candy("Gummy Bear", 7, 12)

def fail():
  first = Cookie("Sugar", 3, 10)
  second = Candy("Sugar", 2, 10)
  assert second.combine(first) == (Candy("Sugar", 5, 10))


if __name__ == "__main__":
  pytest.main([__file__])
