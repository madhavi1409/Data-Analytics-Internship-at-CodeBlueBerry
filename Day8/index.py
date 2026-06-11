# num = 10
# try:
#    print (num/0)
# except ZeroDivisionError:
#    print("number is not divisible by 0 ") 
# print("hello")
# try:
#   print(name)
# except NameError:  
#   print("name not found)
# except:
#   print("an error occured")
try:
  num = 10/0
except:  
  print("an error occurred")