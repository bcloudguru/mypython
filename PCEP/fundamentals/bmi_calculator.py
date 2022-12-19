height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# bmi = kg/m^2
height=float(height)
weight=float(weight)
bmi=round(weight//(height ** 2))
print(bmi)
print(type(bmi))