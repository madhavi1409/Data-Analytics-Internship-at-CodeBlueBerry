try:
  marks = int(input("enter your marks"))
  print("marks", marks)
except ValueError:  
  print("please enter integer values only")