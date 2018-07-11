import random


def generate():
    return random.randint(1, 10)


def guess(correct, counter):
    if counter > 5:
        print('guess failed!')
        exit(0)

    raw = input("please guess:")
    num = raw.strip()
    is_num = is_int(num)
    if not is_num:
        print("please enter correct number.")
        guess(counter, counter)
    gus_num = int(num)
    if gus_num > 10 or gus_num < 1:
        print("please enter number between 1 and 10.")
        guess(counter, counter)

    if gus_num == correct:
        print('correct!')
        exit(0)
    else:
        counter += 1
        guess(correct, counter)


def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


number = generate()
guess(number, 0)
