brunch_items = {'pancake':7.50 , 'waffle':9.00 , 'burger':11.00 , 'home fries':4.50 , 'coffee':1.50 , 'espresso':3.00, 'tea':1.00, 'mimosa':10.50, 'orange juice':3.50}
early_bird_items = {'salumeria plate':8.00, 'salad and breadsticks (serves 2, no refills)':14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu':17.50, 'mushroom ravioli (vegan)':13.50, 'coffee':1.50, 'espresso':3.00}
dinner_items = {'crostininwith eggplant caponata':13.00, 'ceaser salad':16.00, 'pizza with quattro formaggi':11.00, 'duck ragu':19.50, 'mushroom ravioli(vegan)':13.50, 'coffee':2.00, 'espresso':3.00}
kids_items = {'chicken nuggets':6.50, 'fusilli with wild mushrooms':12.00, 'apple juice':3.00}
#7. Give our Menu class a string representation method that will tell you the name of the menu. Also, indicate in this representation when the menu is available.
franchise_items = {'arepa pabellon':7.00, 'pernil arepa':8.50, 'guayanes arepa':8.00, 'jamon arepa':7.50}

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.item = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    reurn("{a} menu available from {b} to {c}".format(a = self.name, b = self.start_time, c = self.end_time))

  def calculate_bill(self, purchase_items):
    total_price = 0
    for item in purchase_items:
      if item in self.items:
        total_prices += self.items[item]
    return(total_price)

class franchise:
  def __init__(self, address, menus):
    self.address = address
    self.manus = menus
    
  def __repr__(self):
    return("The restaurant is in {a}".format(a = self.address))

  def available_menus(self, item):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time < menu.end_time:
        available_menu.append(menu)
      return(available_menu)
      
class Business: 
  def __init__(self, name, franchise):
    self.name = name
    self.franchises = franchises

brunch = menu("brunch", brunch_items, 1100, 1600)
early_bird = Menu("early_bird", early_bird_items, 1500, 1800)
dinner = Menu("dinner", dinner_items, 1700, 2300)
kids = Menu("kids", kids_items, 1100, 2100)
arepas_menu = Menu("franchise", franchise_items, 1000, 2000)
flagship_store = franchise("1232 West End Road",[brunch, early_bird, dinner, kids])
new_isntallment = franchise("12 East Muberry Street", [brunch, early_bird, dinner, kids])
arepas_place = franchise("189 Fitzgerald Avenue", [arepas_menu])
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepas = Business("Take a 'Arepa'", [arepas_place])
print(arepas)