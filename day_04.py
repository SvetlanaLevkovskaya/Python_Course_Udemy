import random


random_integer = random.randint(1, 10)
print(random_integer)

random_float_from_0_to_1 = random.random()
print(random_float_from_0_to_1)
print(random_float_from_0_to_1 * 5)

random_float_from_1_to_5 = random.uniform(1, 5)
print(random_float_from_1_to_5)

love_score = random.randint(1, 100)
print(f"You love score is {love_score}")

