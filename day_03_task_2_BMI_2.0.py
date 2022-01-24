height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kd: "))
bmi = round(weight / height ** 2, 0)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
    print("Your BMI is", bmi, "you are underweight.")
elif bmi == 18.5 or bmi < 25:      # elif bmi < 25
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi == 25 or bmi < 30:        # elif bmi < 30
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi == 30 or bmi < 35:        # elif bmi < 35
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
