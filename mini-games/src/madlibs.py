from collections import deque


def get_word_types(filename):
    word_type_list = []
    with open(filename) as f:
        for line in f:
            word_type_list.append(line)

    return word_type_list


def get_user_input():
    user_input_queue = deque()
    word_type_list = get_word_types('../resource/word_type.txt')
    for word_type in word_type_list:
        prompt = "Enter a {}"
        user_input = input(prompt.format(word_type))
        while not user_input:
            prompt = "Must enter something. Enter a {}"
            user_input = input(prompt.format(word_type))
        user_input_queue.append(user_input)

    return user_input_queue


def fill_story(filename):
    user_input_queue = get_user_input()
    str = ''
    with open(filename) as f:
        for line in f:
            word_list = line.split()
            for word in word_list:
                if '#' in word:
                    word = word.replace('#', user_input_queue.popleft())
                str += word + ' '
        print(str)


fill_story('../resource/story.txt')