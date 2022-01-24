import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_of_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(list_of_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer choice:")
    print(list_of_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("YOU lose")
    elif user_choice > computer_choice:
        print("YOU WIN")
    elif computer_choice > user_choice:
        print("YOU LOSE")
    elif computer_choice == user_choice:
        print("It is a draw")
