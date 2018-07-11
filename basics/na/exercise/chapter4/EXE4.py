# use bucket to sort
# so we only loop through the items and put them in different color bucket
# run with O(n)


def sort_color(mylist):
    n = len(mylist)

    red_list = []
    blue_list = []
    yellow_list = []
    for i in range(0, n):
        if mylist[i][1] == "red":
            red_list.append(mylist[i])
            continue
        if mylist[i][1] == "blue":
            blue_list.append(mylist[i])
            continue
        if mylist[i][1] == "yellow":
            yellow_list.append(mylist[i])
            continue

    # print(red_list)
    # print(blue_list)
    # print(yellow_list)

    return red_list + blue_list + yellow_list

_list = [(1,"blue"), (3,"red"), (4,"blue"), (6,"yellow"), (9,"red")]
print(sort_color(_list))

