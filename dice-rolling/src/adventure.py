
def describe_room():
    room_dict = dict([(1, 'this is room 1'), (2, 'this is room 2'), (3, 'this is room 3')])
    return room_dict


def build_track():
    direction_list = ['left', 'left', 'up']
    # enter room and leave room
    return direction_list


def game(direct_list, rooms, current_loc):
    user_input = input('enter direction (up, down, left, right):')
    if len(direct_list) == 0:
        print('cannot move anymore! game over')
        exit(0)
    item = direct_list.pop(0)
    if user_input == item:
        current_loc += 1  # in room
        output = "you are in room {}. {}"
        print(output.format(current_loc, rooms[current_loc]))
        game(direct_list, rooms, current_loc)
    else:
        print('you can not enter from here.')
        direct_list.insert(0, item)
        game(direct_list, rooms, current_loc)


def start():
    direct_list = build_track()
    rooms = describe_room()
    current_loc = 0
    game(direct_list, rooms, current_loc)


start()
