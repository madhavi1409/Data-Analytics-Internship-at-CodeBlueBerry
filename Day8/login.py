try:
  password = input("enter password")
  if password == "":
    raise Exception("password can't be empty")
  print("invalid login")  
except Exception as e:  
  print(e)