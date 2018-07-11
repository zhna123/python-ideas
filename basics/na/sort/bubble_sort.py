def bubble_sort(list_):
    swapped = True
    j = 0
    while swapped:
        swapped = False;
        j += 1
        for i in range(0, len(list_) - j):
            if list_[i] > list_[i + 1]:
                tmp = list_[i]
                list_[i] = list_[i + 1]
                list_[i + 1] = tmp;
                swapped = True
    return list_

my_list = [3, 4, 1, 9, 2, 4, 3, 7, 8, 0, 3, 5, 1]
print(bubble_sort(my_list))

