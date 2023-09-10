import random as r
class restaurant:
  def __init__(self,food_items):
    self.food_items = food_items

  def show(self):
    for x in self.food_items:
      print(x, end = " | ")

  def show_price(self):
    print("Menu\t\tPrice\n")
    for i in self.food_items:
      print(i,"\t\t",self.food_items[i])

  def invoice_generation(self, data):
      if (data is None):
        print("Requesting order before booking")
      else:
        self.total = 0
        print("---------------------Udupi Palace--------------------")
        print("------------------Invoice Generated------------------")
        print("Invoice no",r.randint(100,999),"\n")
        print ("qty\t\titem\t\tprice\tTotal")
        for i in data:
          print (data[i],'\t\t',i,"\t\t",self.food_items[i],"\t", data[i]*self.food_items[i] )
        for i in data:
          if i in self.food_items.keys():
            self.total = self.total + data[i]*self.food_items[i]
        print ("\nTotal bill amount is ₹",self.total)

class customer:
  def __init__(self):
      self.food_items = {"idly":40,"dosa":80,"pongal":70,"poori":70,"coffee":25,"tea":15}

  def order(self):
    self.dic = {}
    while True:
      self.item = input("enter the item ")
      if self.item in self.food_items.keys():
        self.quantity = int(input("enter the quantity "))
        self.dic[self.item] = self.quantity
      elif self.item == "done":
        break
      else:
        print("The said menu is not available")
    return self.dic

  def reorder(self):
    while True:
      self.item = input("enter the item ")
      if self.item in self.food_items.keys():
        if self.item in self.dic.keys():
          self.quantity = int(input("enter the quantity "))
          self.dic[self.item] = self.dic[self.item] + self.quantity
        else:
          self.quantity = int(input("enter the quantity "))
          self.dic[self.item] = self.quantity
      elif self.item == "done":
        break
      else:
        print("The said menu is not available")
    return self.dic

udupi_palace = restaurant({"idly":40,"dosa":80,"pongal":70,"poori":70,"coffee":25,"tea":15})
hema = customer()

print("""Welcome to udupi palace\n""")
print(""" Use the below mentioned options to serve better
0 Availabe Foods
1 Menucard
2 ordering of food
3 order confirmation
4 Reorder
5 Invoice generation""" )
while True:
  selection = int(input("______________________________\nEnter your requirement \t"))
  if selection == 0:
    udupi_palace.show()
  if selection == 1:
    udupi_palace.show_price()
  if selection == 2:
    print("Once order is done enter 'done'")
    reorder = ""
    order = hema.order()
  if selection == 3:
    print ("your order is")
    for i in order:
      print( order[i],i)
  if selection == 4:
    reorder = hema.reorder()
  if selection == 5:
    if reorder != "":
      bill = udupi_palace.invoice_generation(reorder)
    else:
      bill = udupi_palace.invoice_generation(order)
    break