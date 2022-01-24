# Data Types:
# 1 - Strings
print("Hello"[4])   # subscript
print("123" + "456")  # concatenation

street_name = "Abbey Road"
print(street_name[4] + street_name[7])

# 2 - Integer
print(123_456_789)  # large integer -  underscore is there to make the large number more readable

# 3 - Float
print(type(3.14159))
print(type(734_529.56))
# 4 - Boolean

print("2 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# num_char = len(input("What's your name?"))
# print("Your name has " + str(num_char) + " characters")

print(70 + float("100.5"))

# print("task_1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# two_digit_number = input("Type a two digit number: ")
# print(type(two_digit_number))
# a = int(two_digit_number[0])
# b = int(two_digit_number[1])
# result = a + b
# print(result)

print("Mathematical operation +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(type(6/3))
print(type(2**3))

# PEMDASLR  - rules
# ()
# **
# * /
# + -

print(3 * 3 + 3 / 3 - 3)

print(3 * (3 + 3) / 3 - 3)

# print("task_2 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# height = float(input('enter your height in m: '))
# weight = float(input('enter your weight in kg: '))
# print(int(weight / height ** 2))

print("Number Manipulation ++++++++++++++++++++++++ ++++++++++++++++++++++++++++++")
print(int(8/3), type(8/3))
print(round(8/3), type(round(8/3)))
print(8//3, type(8//3))

result = 4 / 2
result /= 2
print(result)

score = 0
score += 1
print("your score is: " + str(score))

score = 0
height = 1.8
isWinning = True

print("F String in Python ++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(f"Your score is {score} your height is {height} and you are winning is {isWinning}")
