# try:
#   num = (int(input("enter number")))
# except ValueError:  
#   print("invalid number")
# else:  
#   print("you entered", num)
try:
  file = open("dashdata.txt")
  print(file.read())
  
finally:  
  print("program finished")