# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

print("Even or Odd ++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("2 % 2 = 0 # even")
print("3 % 2 = 1 # odd")

print("Nested if statements and elif statement++++++++++++++++++++++++++++")
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoster!")
    age = int(input("What's is your age?"))
    if age < 12:
        print("Please pay $5. ")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")


print("Multiple if statements in Succession ++++++++++++++++++++++++++++")
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoster!")
    age = int(input("What's is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5. ")
    elif age <= 18:
        bill = 12
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")