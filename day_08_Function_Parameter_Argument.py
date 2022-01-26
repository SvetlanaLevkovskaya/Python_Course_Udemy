print("*" * 60)

# Function that allows for input


def greet(name):
    print("Hello", name)
    print(f"How do you do {name}?")
    print("Isn't the weather nice today?")


greet('Svetlana')
greet('Viktor')

print("*" * 60)
# Function with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Svetlana", "Minsk")
print("*" * 60)
greet_with("Minsk", "Svetlana")

print("*" * 60)
# Function with more than 1 input


def greet_with1(name, location):
    print("Hello", name)
    print("What is it like in ", location)

greet_with1( location='Minsk', name='Svetlana')
