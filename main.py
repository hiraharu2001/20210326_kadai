import calc_bmi

h = float(input("身長(m):"))
g = float(input("体重(kg):"))

print(f"BMI:{calc_bmi.bmi(h,g)}")
