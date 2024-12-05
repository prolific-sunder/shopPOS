import pytest
from dessert import DessertItem, IceCream

###############################
# Default value test cases
###############################

def test_IceCream_default():
  ice = IceCream()
  assert ice.name == ""
  assert abs(ice.scoop_count - 0) <= 0
  assert ice.price_per_scoop == pytest.approx(0.0, abs = 10e-3)

##########################3
# Nominal value test cases
###########################

def test_IceCream_default():
  ice = IceCream("Mint", 2, 1.50)
  assert ice.name == "Mint"
  assert abs(ice.scoop_count - 2) <= 0
  assert abs(ice.price_per_scoop - 1.50) <= 0.001

###################################
# Modify attributes test cases
###################################

def test_IceCream_default():
  ice = IceCream()
  ice.name = "Mint"
  assert ice.name == "Mint"
  ice.scoop_count = 2
  assert abs(ice.scoop_count - 2) <= 0
  ice.price_per_scoop = 1.50
  assert abs(ice.price_per_scoop - 1.50) <= 0.001

###################################
# Calculate cost test cases
###################################

def test_IceCream_cost():
  ice = IceCream("Mint", 2, 1.50)
  assert ice.calculate_cost() == pytest.approx((2*1.50), abs=1e-2)

##########################3
# Packaging test case
###########################

def test_IceCream_pack():
  ice = IceCream("Mint", 2, 1.5)
  assert ice.packaging == "Bowl"

if __name__ == "__main__":
  pytest.main([__file__])
