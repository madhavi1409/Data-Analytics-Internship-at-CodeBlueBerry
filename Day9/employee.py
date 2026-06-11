class Employee:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary
  def getSalary(self):  
    print(f"hi!!(self.name) and  your salary is (self.salary)")
obj1 = Employee("rahul",20000)    
obj2 = Employee("amit",30000)
print(obj1.name)
print(obj1.salary)
obj1.getSalary()
#self is super key word
#def __init__(self) is default constructor
#def __init__(self,name,salary) is parameterised constructor
