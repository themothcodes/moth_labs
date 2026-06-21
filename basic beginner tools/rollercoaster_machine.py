print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster:)")
  age = int(input("What is your age?\n"))
  if age <= 12:
    print("Please pay $7")
    bill = 7
  elif age <= 18:
    print("Please pay $9")
    bill = 9
  else:
    print("Please pay $12")
    bill = 12
  pic = str(input("Do you want a picture taken?"))
  if pic == "yes" or pic == "Yes" or pic == "YES":
    bill += 3
  print(f"Your total bill is ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride the rollercoaster.")
  