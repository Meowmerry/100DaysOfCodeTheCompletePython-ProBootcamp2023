################### Scope ####################

enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope can access only inside scope


# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)  # 2


# drink_potion()
# print(potion_strength)  # NameError: name 'potion_strength' is not defined


# Global Scope
player_health = 10


def drink_potion():
    global player_health  # Use the global keyword to modify the global variable
    potion_strength = 2
    player_health += potion_strength
    print(potion_strength)  # 2
    print(player_health)


# drink_potion()

# There is no Block Scope
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]

# if game_level < 5:
#     name_enemy = enemies[0]

# print(name_enemy)


# Modifying Global Scope : Try to not modifying Global Scope varidable
enemies = 1


def increase_enemies():
    # global enemies  # NOT GOOD PRACTICE
    # enemies += 2
    # print(f"enemise inside function : {enemies}")  # 3
    return enemies + 2


enemies = increase_enemies()
# print(f"enemise outside function : {enemies}")  # 3


# Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"


def a_function(a_parameter):
    a_variable = 15
    return a_parameter


a_function(10)
print(a_variable)
