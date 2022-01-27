#############Scope################

# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
# # Local scope
#
#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
#
# drink_potion()

# Global scope

# player_health = 10
#
#
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#
#     drink_potion()


# game_level = 3
# def create_enemy():
#     enemies = ["Sceleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#
#     print(new_enemy)
#
#
# create_enemy()


# Modifying Global scope

# enemies = "Sceleton"
#
#
# def increase_enemies():
#     global enemies
#     enemies = "Zombie"
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")


# enemies = 1
#
#
# def increase_enemies():
#     return enemies + 1
#
#
# # enemies = increase_enemies()
# # print(enemies)
# print(increase_enemies())

# Global Constants
PI = 3.14159
URL = "https://www.google.com"
TWITTER_NANDLE = "@yu_angela"


def a_function(a_parameter):
    a_variable = 15
    return a_parameter



print(a_function())

