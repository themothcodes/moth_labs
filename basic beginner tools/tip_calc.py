greet = "Welcome to the tip calculator!"
print(greet)
amt = float(input("What was the total bill?\nRs. "))
cent =  float(input("How much percent tip would you like to give?\n"))
ppl = int(input("How many people are to split the bill?\n"))
res = ((cent/100 * amt) + amt)/ppl  
print(f"Each person should pay: Rs. {round(res, 2)}")
