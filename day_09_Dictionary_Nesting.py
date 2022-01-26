print('-' * 60)
list_ll = [1, 2, 5, 5]
print(list_ll[3])

print('-' * 60)
dict_dd= {"Bug": "Ann error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code"}

# retrieving items from dictionary
print(dict_dd["Bug"])

print('-' * 60)
# adding new items into dictionary
dict_dd["Loop"] = "The action"
print(dict_dd)

print('-' * 60)
# creating an empty dictionary
empty_dict = {}
print(empty_dict)

print('-' * 60)
# Wipe an existing dictionary
dict_dd = {}
print(dict_dd)

print('-' * 60)
# Edit an item in a dictionary
dict_dd["Bug"] = "sehfhfsfns"
dict_dd["Function"] = "seg/esk/ge"
dict_dd["Loop"] = "dlfgksdkg/s"
print(dict_dd)


print('-' * 60)
# Loop through a dictionary
for key, value in dict_dd.items():
    print(key, value)


print('-' * 60)
# Loop through a dictionary
for key in dict_dd:
    print(key)                 # print key
    print(dict_dd[key])        # print value


# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"]
}


# Nesting a Dictionary in a Dictionary
travel_log1 = {
    "France": {"cities_visited": ["France", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Koln", "Bonn"], "total_visits": 10}

}

# Nesting Dictionary in a List
travel_log2 = [
    {
        "country": "France",
        "cities_visited": ["France", "Lille", "Dijon"],
        "total_visits": 12
    },
        {
        "country": "Germany",
        "cities_visited": ["Berlin", "Koln", "Bonn"],
        "total_visits": 10
    }

]

