# sort the array
# scan the array


def find_mode(mylist):
    sorted_list = sorted(mylist)
    length = len(sorted_list)

    if length == 0:
        return 0
    if length == 1:
        return sorted_list[0]

    counter = 1
    max_counter = 0
    mode = 0
    for i in range(0, length - 1):
        if sorted_list[i + 1] == sorted_list[i]:
            counter += 1
            if i == length - 2:
                if counter > max_counter:
                    max_counter = counter
                    mode = sorted_list[i]
        else:
            if max_counter < counter:
                max_counter = counter
                mode = sorted_list[i]
                counter = 1
    return mode

# my_list = [4, 6, 2, 4, 3, 1, 3, 3, 3, 15, 15, 15, 15, 15, 15, 3, 6]
# print(find_mode(my_list))


# or use a dictionary
# run in O(n)
def find_mode_2(mylist):
    mydict = {}
    for i in range(0, len(mylist)):
        if mylist[i] not in mydict:
            mydict[mylist[i]] = 1
        else:
            mydict[mylist[i]] += 1
    max_freq = (0, 0)
    for key in mydict:
        if mydict[key] > max_freq[1]:
            max_freq = (key, mydict[key])
    return max_freq

my_list = [4, 6, 2, 4, 3, 1, 3, 3, 3, 15, 15, 15, 15, 15, 15, 3, 6]
print(find_mode_2(my_list))


