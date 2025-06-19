# BMI Calculator
# Result = W / {H^2 => h*h}

w = float(input("น้ำหนัก.(กก.)"))
h = float(input("ส่วนสูง.(ซม.)"))

r = w/((h/100)*(h/100))

print(r)