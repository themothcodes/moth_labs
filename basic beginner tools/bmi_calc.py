weight = float(input("enter your weight in kg:\n"))
height = float(input("enter your height in m:\n"))
bmi = weight/(height**height)
print(f"Your BMI is {round(bmi, 2)} kg per metre squared.")
