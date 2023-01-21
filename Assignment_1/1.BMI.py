weight=float(input("please enter your weight(kg): "))
height=float(input("please enter your height(m): "))
BMI=weight/height**2
print(BMI)
if BMI<18.5:
    print("UNDERWEIGHT")
elif BMI<18.5 and BMI>24.9:
    print("NORMAL")
elif BMI<29.9 and BMI>25:
    print("OVERWEIGHT")
elif BMI<34.9 and BMI>30:
    print("OBESE")
elif BMI>35:
    print("EXTREMLY OBESE") 
          
