import random


def dice():
    print(random.randint(1, 6))
    answer = input("Do you want to roll again?")
    if answer.strip().lower() == 'yes':
        dice()
    else:
        return


dice()







