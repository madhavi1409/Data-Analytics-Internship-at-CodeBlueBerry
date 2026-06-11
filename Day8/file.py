try:
  file = open("students.txt")
  print(file.read())
except FileNotFoundError:  
  print("file does not exist")