import random

# letterList = list(range(ord("a"), ord("z")))
# letterList.append(ord(" "))
# print(letterList)


def generate(in_position_dict):
    letter_list = list(range(ord("a"), ord("z")))
    letter_list.append(ord("z"))
    letter_list.append(ord(" "))
    char_list = ['0'] * 28
    for i in range(28):
        if i in list(in_position_dict.keys()):
            char_list[i] = in_position_dict.get(i)
        else:
            char_list[i] = chr(random.choice(letter_list))

    return ''.join(char_list)

# print(generate())


def score(generated):
    goal = "methinks it is like a weasel"
    word_score = 0;
    in_position_dict = {}
    for i in range(len(goal)):
        if goal[i] == generated[i]:
            word_score += 1
            in_position_dict[i] = generated[i]
    return word_score, in_position_dict


def match():
    perfect_score = 28
    tries = 0
    max_score = 0
    in_position_dict = {}
    generated = generate(in_position_dict);
    (current_score, in_position_dict) = score(generated);
    while current_score != perfect_score:
        tries += 1
        if current_score > max_score:
            max_score = current_score
        if tries % 1000 == 0:
            print("current best score is %d after %d tries" % (max_score, tries))
        generated = generate(in_position_dict)
        (current_score, in_position_dict) = score(generated);
    print("strings match after %d tries; the generated string is %s" % (tries, generated))

print(match())


    


