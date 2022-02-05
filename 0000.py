import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# print("Welcome!")
a = int(input("how many letters would you like in your password?\n"))
b = int(input("how many symbols would you like?\n"))
c = int(input("how many numbers would you like?\n"))

# password = ''
# for letter in range(0, a+1):
#     password += random.choice(letters)
# for symbol in range(0, b+1):
#     password += random.choice(symbols)
# for number in range(0, c+1):
#     password += random.choice(numbers)
#
# print(f"Here is you password {password}")

password_list = []
for letter in range(0, a+1):
    password_list.append(random.choice(letters))
for symbol in range(0, b+1):
    password_list.append(random.choice(symbols))
for number in range(0, c+1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for item in password_list:
    password += item
print(f"Here is you password {password}")



