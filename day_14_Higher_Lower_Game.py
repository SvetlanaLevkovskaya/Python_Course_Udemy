from day_14_art import logo, vs
from game_data import data
import random
# from replit import clear


def format_data(account):
    """ 3. Format the account data into a printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it correct"""
    if a_followers > b_followers:
        if guess == "a":
            return guess == "a"
        else:
            return guess == "b"


# 1. Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# 8. Make the game repeatable
while game_should_continue:
    # 2. Generate a random account from the game

    # 9. Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # 4. Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # 5. Check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    ## Get follower count of each account
    ## Use if statement to check if user is correct

    # 10. Clear the screen between rounds
    print("\033[H\033[2J", end="", flush=True)
    print(logo)

    # 6. Give user feedback on their guess
    # 7. Score keeping
    if is_correct:
        score += 1
        print(f"Yoy right! Your current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
