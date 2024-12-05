import pytest
from dessert import DessertItem, Sundae

###############################
# Default value test cases
###############################

def test_sundae_default(): 
  sundae = Sundae()
  assert sundae.name == ""
  assert abs(sundae.scoop_count - 0) <= 0
  assert sundae.price_per_scoop == pytest.approx(0.0, abs = 10e-3)
  assert sundae.topping_name == ""
  assert sundae.topping_price == pytest.approx(0.0, abs = 10e-3)

##########################3
# Nominal value test cases
###########################

def test_sundae_default(): 
  sundae = Sundae("Mint", 2, 1.50, "gummy bear", 0.50)
  assert sundae.name == "Mint"
  assert abs(sundae.scoop_count - 2) <= 0
  assert abs(sundae.price_per_scoop - 1.50) <= 0.001
  assert sundae.topping_name == "gummy bear"
  assert abs(sundae.topping_price - 0.50) <= 0.001

###################################
# Modify attributes test cases
###################################

def test_sundae_default(): 
  sundae = Sundae()
  sundae.name = "Mint"
  assert sundae.name == "Mint"
  sundae.scoop_count = 2
  assert abs(sundae.scoop_count - 2) <= 0
  sundae.price_per_scoop = 1.50
  assert abs(sundae.price_per_scoop - 1.50) <= 0.001
  sundae.topping_name = "gummy bear"
  assert sundae.topping_name == "gummy bear"
  sundae.topping_price = 0.50
  assert abs(sundae.topping_price - 0.50) <= 0.001

###################################
# Calculate cost test cases
###################################

def test_sundae_cost():
  sundae = Sundae("Mint", 2, 1.50, "gummy bear", 0.50)
  assert sundae.calculate_cost() == pytest.approx((2*1.50) + 0.50, abs=1e-2)

##########################3
# Packaging test case
###########################

def test_Sundae_pack():
  sun = Sundae("Mint", 2, 1.50, "gummy bear", 0.50)
  assert sun.packaging == "Boat"
  
if __name__ == "__main__":
  pytest.main([__file__])
