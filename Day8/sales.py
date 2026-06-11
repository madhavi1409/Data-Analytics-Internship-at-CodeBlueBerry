sales = ["1000", "2000", "abc", "1500"]
total = 0
for item in sales:
  try:
    total += int(item)
  except ValueError:  
    print("invalid sales data", item)
  print(total)  
