number_1 = float(input("What's the first number?: "))
sing = ["+", "-", "*", "/"]
for i in sing:
    print(i)

calc_finished = False


def my_calc(number_1, number_2):
    if pick_operator == "+":
        return number_1 + number_2
    elif pick_operator == "-":
        return number_1 - number_2
    elif pick_operator == "*":
        return number_1 * number_2
    elif pick_operator == "/":
        return number_1 / number_2
    else:
        return "Enter a valid operator"


while not calc_finished:
    pick_operator = input("Pick an operation: ")
    number_2 = float(input("What's the second number?: "))
    print(my_calc(number_1, number_2))
    calc_continue = input("Type 'y' to calculating with 10.0, or type 'n' to start a new calculation: ")
    if calc_continue == 'n':
        break





