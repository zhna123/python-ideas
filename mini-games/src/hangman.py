import random


def get_a_word():
    word_list = ['happy']
    index = random.randint(0, len(word_list) - 1)
    return word_list[index]


def game(word_dict, count, guessed_letter_list):

    if len(word_dict) == 0 & count <= 10:
        print("you guessed it!")
        return

    if count > 10:
        print('exceed the maximum times to try.')
        exit(0)

    letter = input('enter a single letter')
    if letter in guessed_letter_list:
        print('you already guessed this letter')
        game(word_dict, count, guessed_letter_list)

    guessed_letter_list.append(letter)
    count += 1
    if letter in word_dict.keys():
        message = "letter {} appears in location: {}"
        print(message.format(letter, word_dict[letter]))
        del word_dict[letter]
        game(word_dict, count, guessed_letter_list)

    else:
        game(word_dict, count, guessed_letter_list)


# how many times a letter appear
def get_letter_appear_dict(split_word):
    letter_appear_dict = dict()
    for l in split_word:
        if l in letter_appear_dict.keys():
            letter_appear_dict[l] += 1
        else:
            letter_appear_dict[l] = 1
    return letter_appear_dict


# which locations a letter appears at
def get_letter_index_dict(split_word):
    letter_index_dict = dict()
    for ind, l in enumerate(split_word):
        if l in letter_index_dict.keys():
            letter_index_dict[l].append(ind)
        else:
            letter_index_dict.update({l: [ind]})
    return letter_index_dict


def play():
    word = get_a_word()
    split_word = list(word)
    # can also create a dict: letter -> times of appearance to record
    # how many times a certain letter appears
    # furthermore, the appearance locations can be recorded too

    # word_set = set(split_word)
    word_dict = get_letter_index_dict(split_word)
    guessed_letter_list = []

    game(word_dict, 0, guessed_letter_list)
    print('the word is ' + word)


play()
