import pytest
from dessert import DessertItem, Candy

def test_dessertitem_default():
  dessert = Candy()
  assert dessert.name == ""

def test_dessertitem():
  dessert = Candy("gummy bears")
  assert dessert.name == "gummy bears"
  
def test_dessertitem_modify():
  dessert = Candy("gummy bearz")
  assert dessert.name == "gummy bearz"

  dessert.name = "Bannana Split"
  assert dessert.name == "Bannana Split"

def test_calculate_tax():
  dessert = Candy("gummy bears", 3, 12.00)
  assert dessert.calculate_tax() == pytest.approx((3.0 *12.00) * (7.25/100), abs=1e-2)

def test_equality():
  dessert = Candy("gummy bears", 2, 4)
  other = Candy("candy corn", 4, 2)
  assert dessert.__eq__(other) == True
#########################################invisible semi colon?:
def test_inequality():
  dessert = Candy("gummy bears", 3, 12)
  other = Candy("candy corn", 4, 2)
  assert dessert.__ne__(other) == True

def test_less():
  dessert = Candy("gummy bears", 4, 2)
  other = Candy("candy corn", 12, 2)
  assert dessert.__lt__(other) == True

def test_greater():
  dessert = Candy("gummy bears", 3, 12)
  other = Candy("candy corn", 4, 2)
  assert dessert.__gt__(other) == True

def test_le():
  dessert = Candy("gummy bears", 3, 12)
  other = Candy("candy corn", 12, 3)
  other2 = Candy("thingy", 10, 10)
  assert dessert.__le__(other) == True
  assert dessert.__le__(other2) == True

def test_ge():
  dessert = Candy("gummy bears", 3, 12)
  other = Candy("candy corn", 12, 3)
  other2 = Candy("gummy bears", 2, 2)
  assert dessert.__ge__(other) == True
  assert dessert.__ge__(other2) == True



if __name__ == "__main__":
  pytest.main([__file__])
