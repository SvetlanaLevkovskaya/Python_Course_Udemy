# Functions with Outputs

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    print(f"{formatted_f_name} {formatted_l_name}")


format_name("sVeTa", "LeVkoVskaya")


def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name("sVeTa", "LeVkoVskaya")
print(formatted_string)

print(format_name("sVeTa", "LeVkoVskaya"))


def format_name(f_name, l_name):                       # return as an early exit
    """ Take a first and lst name and format it to
    return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result:{formatted_f_name} {formatted_l_name}"


print(format_name(input("What is your first name? "),    # printing outputs directly
                  input("What is your last name? ")))

length = len("formatted_f_name")                  # Already used functions with Outputs
print(length)
