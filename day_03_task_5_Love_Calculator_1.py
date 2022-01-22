"""You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number."""


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

check_T = (name1 + name2).upper().count('T')
check_R = (name1 + name2).upper().count('R')
check_U = (name1 + name2).upper().count('U')
check_E = (name1 + name2).upper().count('E')
check_TRUE = int(check_T+check_R+check_U+check_E)
# print(check_TRUE)
check_L = (name1 + name2).upper().count('L')
check_O = (name1 + name2).upper().count('O')
check_V = (name1 + name2).upper().count('V')
check_E = (name1 + name2).upper().count('E')
check_LOVE = int(check_L+check_O+check_V+check_E)
# print(check_LOVE)
love_score = int(str(check_TRUE) + str(check_LOVE))
#print(type(love_score))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


# David Beckham = 4
# Viktoria Beckham  = 5
# total = 45