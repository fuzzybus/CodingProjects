height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are under weight.\n")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you are in the normal range.\n")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight.\n")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.\n")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.\n")
    
