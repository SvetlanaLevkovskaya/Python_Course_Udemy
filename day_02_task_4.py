print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_per_person = total_bill * tip / 100 / people
print(f"Each person should pay: ${tip_per_person:.2f}")
# print(type(total_bill))
# print(type(tip))
# print(type(tip_per_person))

a_float = 3.14159
limited_float = "{:.2f}".format(a_float)


a = 13.946
print(a)
# 13.946
print("%.2f" % a)
# 13.95
round(a,2)
# 13.949999999999999
print("%.2f" % round(a, 2))
# 13.95
print("{:.2f}".format(a))
# 13.95
print("{:.2f}".format(round(a, 2)))
# 13.95
print("{:.15f}".format(round(a, 2)))
# 13.949999999999999
