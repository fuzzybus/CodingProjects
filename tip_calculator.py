# Tip Calculator
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
guests = int(input("How many people are splitting the bill? "))
tip = total_bill / tip_percentage
to_pay = (total_bill + tip) / guests
to_pay = (round(to_pay, 2))
print(f"Each person should pay ${to_pay}")


