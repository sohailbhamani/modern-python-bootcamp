# This file receives age input from the user and determines a status

# This code is more basic and only handles blank ages but not strings
# i.e. ValueError
# age = input("How old are you? ")

# # determine result
# if age:
#     age = int(age)
#     if age >= 21:
#         # 21+ = drink, normal entry
#         print("You can enter and drink")
#     elif age >= 18:
#         # 18-21 = wristband
#         print("You can enter, but need a wristband")
#     else:
#         # too young, sorry
#         print("You are too young, sorry")
# else:
#     print("Please enter an age!")

# This method handles the ValueError and is more streamlined
try:
    age = int(input("How old are you? "))

    # determine result
    if age >= 21:
        # 21+ = drink, normal entry
        print("You can enter and drink")
    elif age >= 18:
        # 18-21 = wristband
        print("You can enter, but need a wristband")
    else:
        # too young, sorry
        print("You are too young, sorry")
except ValueError:
    print("You must use an integer")
