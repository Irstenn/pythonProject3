# name = input("what's your name? ")
# favorite_color = input("what's your favorite color? ")
# print(name + ' aime la couleur ' + favorite_color)
#
# print("__________________________________________")
#
# birthday_age = input("Enter your birthday age please !!! ")
# age = 2021 - int(birthday_age)
# print(f'{name} vous aviez normalement {age} ans')
# print(name + ' vous aimiez reellement ' + favorite_color)
#
# print("_" * 20)

# user_weight = input('quel est ton poids en gramme ? ')
# weight_to_kg = int(user_weight) * 100
# print(f"votre poids en kilogramme est: {weight_to_kg}")
#
# print("______________________________________________________")
# # conversion du poids en kg ou pounds
# poids_user = int(input("quel est votre poids ?"))
# unit_poids = input("(L)bs or (K)g ")
# if poids_user == 'K':
#     print(f"Votre poids est de {poids_user * 0.45} kilos")
# else:
#     print(f"Votre poids est de {poids_user / 0.45} pounds")

print("______________________________________________________")


# recherche du nombre mystere
# user must find a mysterious number by playing only 3 times. If he failed then the program sends a message you've fail
# mysterious_number = 9
# limit_type = 3
# enter_number = 0
#
# while enter_number < limit_type:
#     user_guess = int(input("Guess: "))
#     enter_number += 1
#     if user_guess == mysterious_number:
#         print("Ouraaaaaa you won the game ")
#         break
# else:
#     print("Sorry buhh you failed !")
#
# print("________________________________________")

# a car game that uses 3 words: start,stop,help  and also quit when a user type 4 of these words
# command = ""
# started = False
# while True:
#     command = input('Please type one of the 3 words > ').lower()
#     if command == "start":
#         if started:
#             print("Car already started.")
#         else:
#             started = True
#             print("car started.")
#     elif command == "stop":
#         if not started:
#             print("car is already stopped.")
#         else:
#             started = False
#             print("Car is stopped.")
#     elif command == "help":
#         print("""
# first - start the car
# second - stop a car
# third - quit a car
#         """)
#     elif command == "quit":
#         print("You have quit the car")
#         break

# using of nested loop
# for x in range(4):
#     for y in range (3):
#         print(f"({x}, {y})")

# # dictionary
# user_number = input("Enter the numbers please: ")
# numbers = {
#     "1": "one",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = ""
# for ch in user_number:
#     output += numbers.get(ch, "!") + " "
# print(output)

def find_maximum(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

