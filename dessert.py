from abc import ABC, abstractmethod
from packaging import Packaging
from payment import PayType, Payable
from combine import Combinable

class DessertItem(ABC, Packaging):

  def __init__(self, name: str = "", tax_percent: float = 7.25):
    self.name = name
    self.tax_percent = tax_percent
    self.packaging = None

  def __str__(self):
    return f"{self.name}"
  
  @abstractmethod
  def calculate_cost(self):
    pass
  
  def calculate_tax(self):
    return round((self.tax_percent/100) * self.calculate_cost(), 2)
  
  def __eq__(self, other):
    return self.calculate_cost() == other.calculate_cost()

  def __ne__(self, other):
    return self.calculate_cost() != other.calculate_cost()

  def __lt__(self, other):
    return self.calculate_cost() < other.calculate_cost()

  def __gt__(self, other):
    return self.calculate_cost() > other.calculate_cost()

  def __le__(self, other):
    return self.calculate_cost() <= other.calculate_cost()

  def __ge__(self, other):
    return self.calculate_cost() >= other.calculate_cost()

###########
#Candy Class
###########

class Candy(DessertItem):
  def __init__(self, name: str = "", candy_weight: float = 0.0, price_per_pound: float = 0.0, packaging: str = "Bag"):
    super().__init__(name) 
    self.candy_weight = candy_weight
    self.price_per_pound = price_per_pound
    self.packaging = packaging
  
  def can_combine(self, other:"Candy") -> bool:
    if isinstance(other, Candy) and self.name == other.name and self.price_per_pound == other.price_per_pound:
      return True
    else:
      return False

  def combine(self, other: "Candy") -> "Candy":
    return Candy(self.name, self.candy_weight + other.candy_weight, self.price_per_pound)

  def calculate_cost(self):
    return round(self.candy_weight * self.price_per_pound, 2)

  def __str__(self):
    return f"{self.name} ({self.packaging}), {self.candy_weight} lbs, ${self.price_per_pound}/lb, ${self.calculate_cost()}, ${self.calculate_tax()}"
  
#############
#Cookie Class
#############

class Cookie(DessertItem):
  def __init__(self, name: str = "", cookie_quantity: int = 0, price_per_dozen: float = 0.0, packaging: str = "Box"):
    super().__init__(name)
    self.cookie_quantity = cookie_quantity
    self.price_per_dozen = price_per_dozen
    self.packaging = packaging
  
  def can_combine(self, other:"Cookie") -> bool:
    if isinstance(other, Cookie) and self.name == other.name and self.price_per_dozen == other.price_per_dozen:
      return True
    else:
      return False

  def combine(self, other: "Cookie") -> "Cookie":
    return Cookie(self.name, self.cookie_quantity + other.cookie_quantity, self.price_per_dozen)
  
  def calculate_cost(self):
    return round((self.cookie_quantity/12) * self.price_per_dozen, 2)
  
  def __str__(self):
    return f"{self.name} ({self.packaging}), {self.cookie_quantity} cookies, ${self.price_per_dozen}/dozen, ${self.calculate_cost()}, ${self.calculate_tax()}"
  
###############
#IceCream Class
###############

class IceCream(DessertItem):
  def __init__(self, name: str = "", scoop_count: int = 0, price_per_scoop: float = 0.0, packaging: str = "Bowl"):
    super().__init__(name)
    self.scoop_count = scoop_count
    self.price_per_scoop = price_per_scoop
    self.packaging = packaging
  
  def can_combine(self, other:"IceCream") -> bool:
    return False
  
  def calculate_cost(self):
    return round(self.scoop_count * self.price_per_scoop, 2)
  
  def __str__(self):
    return f"{self.name} ({self.packaging}), {self.scoop_count} scoops, ${self.price_per_scoop}/scoop, ${self.calculate_cost()}, ${float(self.calculate_tax())}"

###############
#Sundae Class
###############

class Sundae(IceCream):
  def __init__(self, name: str = "", scoop_count: int = 0 , price_per_scoop: float = 0.0, topping_name: str = "", topping_price: float = 0.0, packaging: str = "Boat"):
    super().__init__(name, scoop_count, price_per_scoop)
    self.topping_name = topping_name
    self.topping_price = topping_price
    self.packaging = packaging

  def can_combine(self, other:"Sundae") -> bool:
    return False
  
  def calculate_cost(self):
    IceCreamCost = super().calculate_cost()
    return round(IceCreamCost + self.topping_price, 2)
  
  def __str__(self):
    return f"{self.topping_name} {self.name} ({self.packaging}), {self.scoop_count} scoops, ${self.price_per_scoop}/scoop, ${self.calculate_cost()}, ${self.calculate_tax()}, {self.topping_name}, 1, {self.topping_price}"

###############
#Order Class
###############

class Order():
  def __init__(self, pay_type = PayType.CASH):
    self.order = []
    self.pay_type = pay_type
    self.receipt = []
  
  def __iter__(self):
    self.index = 0
    return self

  def __next__(self):
    if self.index > len(self)-1:
      raise StopIteration
    item = self.order[self.index]
    self.index +=1
    return item


  def add(self, object):
    combining = False
    if isinstance(object, (IceCream, Sundae)):
      pass
    else:
      for exist_item in self.order:
        if exist_item.can_combine(object):
          new_item = exist_item.combine(object)
          self.order.remove(exist_item)
          self.order.append(new_item)
          combining = True
          break
    if combining is False:
      self.order.append(object)
    
  def __len__(self):
    return len(self.order)
  
  def order_cost(self):
    order_cost = 0
    for item in self.order:
      order_cost += item.calculate_cost()
    return round(order_cost, 2)
  
  def order_tax(self):
    order_tax = 0 
    for item in self.order:
      order_tax += item.calculate_tax()
    return round(order_tax, 2)                ##is important to note that the round() method causes some weird rounding around the .5 mark

  def get_pay_type(self):
    if self.pay_type.name not in ("CASH", "CARD", "PHONE"):
      raise ValueError
    return self.pay_type
  
  def set_pay_type(self, new_type):
    if new_type.name not in ("CASH", "CARD", "PHONE"):
      raise ValueError
    self.pay_type = new_type
  
  def sort_order(self):
    for item in self.order:         #if the for loop isn't implemented, only does the first 2 items
      self.order.sort()      


  def for_receipt(self):
    self.sort_order()
    #Format MUST stay as 2D lists. The lists have to be comma seperate for each table item
    #This is all a really big mess but I was having trouble with creating the formatting needed for receipt.py
    #All append items must be within [] brackets or the 2D list won't be retained
    for item in self.order:
      if isinstance(item, Sundae):            #isinstance to check which class so I can use the right {thingy}
        self.receipt.append([f"{item.topping_name} {item.name} Sundae ({item.packaging})", f"{item.scoop_count} scoops", f"${item.price_per_scoop}/scoop", f"${item.calculate_cost()}", f"${item.calculate_tax()}"])
        self.receipt.append([f"{item.topping_name}", "1", f"{item.topping_price}"])
      elif isinstance(item, Candy):
        self.receipt.append([f"{item.name} ({item.packaging})", f"{item.candy_weight} lbs", f"${item.price_per_pound}/lb", f"${item.calculate_cost()}", f"${item.calculate_tax()}"])
      elif isinstance(item, Cookie):
        self.receipt.append([f"{item.name} Cookies ({item.packaging})", f"{item.cookie_quantity} cookies", f"${item.price_per_dozen}/dozen", f"${item.calculate_cost()}", f"${item.calculate_tax()}"])
      elif isinstance(item, IceCream):
        self.receipt.append([f"{item.name} Ice Cream ({item.packaging})", f"{item.scoop_count} scoops", f"${item.price_per_scoop}/scoop", f"${item.calculate_cost()}", f"${item.calculate_tax()}"])
    return self.receipt
    
  def __str__(self):
    #I realize my naming was not very specific, str is for the full return of all order things, string is for just the singular item string
    str = ""
    for item in self.order:
      string = item.__str__()
      str += string
    str += f"Paid by {self.pay_type}"
    return str
