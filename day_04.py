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

print("Lists+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
print("************************************************************************************")
print("                                                                                     ")
print(states_of_america)
print(states_of_america[0])

name = states_of_america[-1]
print("************************************************************************************")
print("                                                                                     ")
states_of_america[0] = "Minsk"
print(states_of_america)

print("************************************************************************************")
print("                                                                                     ")
states_of_america.append("Belarus")
print(states_of_america)
print("************************************************************************************")
print("                                                                                     ")
states_of_america.extend(["skdjhfkjshfkj", "ksjfhkjhsfk"])
print(states_of_america)

print(len(states_of_america))
print("************************************************************************************")
print("                                                                                     ")

a = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']

print(a)
for i in range(5):
    print(random.choice(a))

print("************************************************************************************")
print("                                                                                     ")
num_of_states = len(states_of_america)
print(num_of_states)
print(states_of_america[53-1])
print("************************************************************************************")
print("                                                                                     ")

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
               "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen1 = [fruits, vegetables]
print(dirty_dozen1[1])


