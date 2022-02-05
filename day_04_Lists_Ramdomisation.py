import random


random_integer = random.randint(1, 10)
print(random_integer)

random_float_from_0_to_1 = random.random()
print(random_float_from_0_to_1)
print(random_float_from_0_to_1 * 5)

random_float_from_1_to_5 = random.uniform(1, 10)
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

print("************************************************************************************")
print("                                                                                     ")
# random.seed(2)

# Get the state of the generator
state = random.getstate()

print('Generating a random sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))

# Restore the state to a point before the sequence was generated
random.setstate(state)
print('Generating the same identical sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))

print("************************************************************************************")
print("                                                                                     ")

q = random.random()
print(q)
x = random.randint(5, 10)
print(x)
v = random.randrange(11, 111, 10)
print(v)
c = random.uniform(1, 25)
print(c)
ll = [1,2,3,'one', 'two']
ll.append('three')
print(ll)
ll.extend(['four', 'five'])
print(ll)
ll.insert(5, 'insert')
print(ll)
ll.remove('five')
print(ll)
ll.pop(1)
print(ll)
# ll.clear()
# print(ll)
# del ll[:]
# print(ll)
index = ll.index('four')
print('index = ', index)
print(ll.count('two'))
ll_1 = [5, 4, 1, 2, 58, 55]
ll_1.sort()
print(ll_1)
ll_1.reverse()
print(ll_1)
ll_2 = ll_1.copy()
print(ll_2)
print(ll_1)

print("************************************************************************************")
print("                                                                                    ")

a = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(a)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

print("************************************************************************************")
print("                                                                                    ")

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_vec = [num for elem in vec for num in elem]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(vec)
print(new_vec)

print("************************************************************************************")
print("                                                                                    ")
a = "Python is great"
print(a.split())

b = "Python, is, great"
print(b.split(', '))

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(',')
# print(names)

# names_string = input("type a word. ")
# print(list(names_string))


string1 = "12345678"
#coverting the string into list of strings
list1 = list(string1)
print("Converted string to list : ", list1)
#typecasting the individual elements of the string list into integer using the map() method
list2 = list(map(int, list1))
print("List of integers : ", list2)

string1 = "1 2 3 4 5 6 7 8"
#coverting the string into list of strings
list1 = list(string1.split())
print("Converted string to list : ", list1)
#typecasting the individual elements of the string list into integer using the map() method
list2 = list(map(int, list1))
print("List of integers : ", list2)

string1 = "This is Python"
#converting string1 into a list of strings
# string1 = string1.split()
#applying list method to the individual elements of the list string1
list1 = list(map(list, string1.split()))
print(f"Converted to list of character list:\n{list1}")
