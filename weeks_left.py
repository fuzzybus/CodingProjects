# Your life in weeks

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

life = 90 - int(age)

days = life * 365
weeks = life * 52
months = life * 12


print(f"You have {days} days, {weeks} weeks, and {months} months left.")
