class Bank:
  def __init__(self,account_holder,balance):
    self.account_holder = account_holder
    self.balance = balance
  def display(self):  
    print("name of account holder is", self.account_holder)
    print("the account balance is", self.balance)
bank = Bank("rahul", 50000)    
bank1 = Bank("aman", 20000)
bank.display()
bank1.display()