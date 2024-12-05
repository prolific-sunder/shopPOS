from dessert import DessertItem, Candy, Cookie, IceCream, Sundae, Order
import receipt
from payment import PayType, Payable

class Customer():
  id: int = 1000
  
  def __init__(self, customer_name: str):
    self.customer_name = customer_name
    self.order_history = []
    Customer.id += 1
    self.customer_id = Customer.id

  def add2history(self, order: 'Order') -> 'Customer':
    self.order_history.append(order)
    return self

class DessertShop():

  customer_db : dict[str, Customer] = {

  }
  ############
  #FOR CANDY 
  ############

  def user_prompt_candy(self):
    
    name = input("Enter the type of candy: ")

    while True:
      try:
        candy_weight = float(input("Enter the candy weight: "))
        break
      except ValueError:
        print("Error: Please enter a valid number")

    while True:
      try:
        candy_price = float(input("Enter the price per pound: "))
        break
      except ValueError:
        print("Error: Please enter a valid number")

    return Candy(name, candy_weight, candy_price)


  ############
  #FOR COOKIE
  ############

  def user_prompt_cookie(self):
    
    name = input("Enter the type of cookie: ")

    while True:
      try:
        cookie_quantity = int(input("Enter the quantity purchased: "))
        break
      except ValueError:
        print("Error: Please enter a valid whole number")

    while True:
      try:
        cookie_price = float(input("Enter the price per dozen: "))
        break
      except ValueError:
        print("Error: Please enter a valid number")
    
    return Cookie(name, cookie_quantity, cookie_price)

  ############
  #FOR ICECREAM
  ############

  def user_prompt_icecream(self):
    
    name = input("Enter the type of ice cream: ")

    while True:
      try:
        scoops = int(input("Enter the number of scoops: "))
        break
      except ValueError:
        print("Error: Please enter a valid whole number")

    while True:
      try:
        scoop_price = float(input("Enter the price per scoop: "))
        break
      except ValueError:
        print("Error: Please enter a valid number")
    
    return IceCream(name, scoops, scoop_price)

  ############
  #FOR SUNDAE
  ############

  def user_prompt_sundae(self):

    name = input("Enter the type of ice cream: ")

    while True:
      try:
        scoops = int(input("Enter the number of scoops: "))
        break
      except ValueError:
        print("Error: Please enter a valid whole number")

    while True:
      try:
        scoop_price = float(input("Enter the price per scoop: "))
        break
      except ValueError:
        print("Error: Please enter a valid number")
    
    topping = input("Enter the topping: ")

    while True:
      try:
        topping_price = float(input("Enter the price for the topping: "))
        break
      except ValueError:
        print("Error: Please enter a valid number")

    return Sundae(name, scoops, scoop_price, topping, topping_price)

  ##################
  ##PAYMENT METHOD
  ##################

  def prompt_pay(self):
    while True:
      try:
        choice = int(input("1: Cash \n2: Card\n3: Phone \nEnter payment method: "))
        if choice not in (1, 2, 3):
          raise ValueError("Enter 1 - 3")
      except ValueError:
        print("Invaild input, please try again")
      else:
        break
    return choice


################
#MAIN FUNCTION
################

def main():
  shop = DessertShop() 
  request = Order()

  ##############
  #UI INTERFACE 
  ##############
  repeat: bool = False
  while not repeat:
    # boolean done = false
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
            '1: Candy',
            '2: Cookie',
            '3: Ice Cream',
            '4: Sundae',
            '\nWhat would you like to add to the order? (1-4, Enter for done): '
      ])

    while not done:
      choice = input(prompt)
      match choice:
        case '':
          done = True
        case '1':            
          item = shop.user_prompt_candy()
          request.add(item)
          print(f'{item.name} has been added to your order.')
        case '2':            
          item = shop.user_prompt_cookie()
          request.add(item)
          print(f'{item.name} has been added to your order.')
        case '3':            
          item = shop.user_prompt_icecream()
          request.add(item)
          print(f'{item.name} has been added to your order.')
        case '4':            
          item = shop.user_prompt_sundae()
          request.add(item)
          print(f'{item.name} has been added to your order.')
        case _:            
          print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')
    
    customer_name = input("Enter the customer's name: ")
    if customer_name not in DessertShop.customer_db:
      specific = Customer(customer_name)
      DessertShop.customer_db[customer_name] = id(specific)
    else:
      specifc = DessertShop.customer_db[customer_name]

    specific.add2history(request)
    
    payment = shop.prompt_pay()
    request.set_pay_type(PayType(payment))


  ##############
  #MAKE RECEIPT
  ##############

    data = [
      [f"Customer Name: {specific.customer_name}", f"Customer ID: {specific.customer_id}", f"Total Orders: {len(specific.order_history)}"],
      ["Name" , "Quantity", "Unit Price", "Cost" , "Tax"]
    ]
    #REMINDER, DATA MUST REMAIN A 2D LIST, all added items must be added as a new list
    for item in request.for_receipt():
      data.append(item)

    data.append(["Order Subtotals", "" , " ", f"${request.order_cost()}", f'${request.order_tax()}'])
    data.append(["Order Total", "", "", "", f"${round(request.order_cost() + request.order_tax(), 2)}"])        # "" is just to align the things to proper column
    data.append(["Total items in the order", f"{request.__len__()}"])
    data.append([f"Paid with {request.get_pay_type().name}"])

    receipt.make_receipt(data)


  ######
  #Another
  ######
    answer = input("Would you like to start another order? (y/n) ")
    match answer:
      case 'y':
        repeat = False
        request.order = []
        request.receipt = []
        data = [
          ["Name" , "Quantity", "Unit Price", "Cost" , "Tax"]
        ]
      case 'n':
        repeat = True  
      case _:
        print('Invalid response:  Please enter y or n')

if __name__ == "__main__":
   main()
