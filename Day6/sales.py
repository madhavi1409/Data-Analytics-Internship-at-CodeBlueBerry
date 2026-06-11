file = open("sales.txt", "w")
file.write("1000\n")
file.write("2000\n")
file.write("1500\n")
file.write("3000\n")
file.write("2500\n")
file.close()
print("Sales Data Saved")


file = open("sales.txt", "r")
file.close()
total = 0
with open("sales.txt", "r") as file:
  for line in file:
   total += int(line)
print("Total Sales =", total)

