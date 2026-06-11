class Product:
  def __init__(self,product_name,price):
    self.product_name = product_name
    self.price = price
  def display(self):  
    print("name of product is", self.product_name)
    print("price of the product", self.price)
product = Product("laptop", 50000)    
product = Product("mobile phone", 20000)
product.display()