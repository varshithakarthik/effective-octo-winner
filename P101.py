import random

response = "y"

while response == "y":
    num = random.randint(1,6)
    if num == 1:
        print("The number on the dice is 1")
    if num == 2:
        print("The number on the dice is 2")
    if num == 3:
        print("The number on the dice is 3")
    if num == 4:
        print("The number on the dice is 4")
    if num == 5:
        print("The number on the dice is 5")
    if num == 6:
        print("The number on the dice is 6")

    response = input('Do you want to roll the dice? y or n? ')
    print('\n')