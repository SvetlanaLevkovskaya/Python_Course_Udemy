for i, j in enumerate(['foo', 'bar', 'baz']):
    if j == 'bar':
        print(i)

mylist = ["foo", "bar", "baz", "bar"]
newlist = enumerate(mylist)
for index, item in newlist:
    if item == "bar":
        print(index, item)

starting_dictionary = {
    "a": 9,
    "b": 8,
}


# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }

starting_dictionary["c"] = 7
final_dictionary = starting_dictionary

print(final_dictionary)


dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# dict["c"] = [1, 2, 3]
# for key in dict:
#     dict[key] += 1
# dict[1] = 4
print(dict['a'])

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2])
print(order["main"][2][0])
# print(order["dessert" - 1][2][0])  # incorrect


def add(n1, n2):
    return n1 + n2


print(add(1, 2))

for _ in range(5):
    print(_)

print("-" * 60)


def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)


result = outer_function(5, 10)
print(result)

print("-" * 60)


def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
    

print(my_function(25))


