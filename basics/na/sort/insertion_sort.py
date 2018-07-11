def insertion_sort(list_):
    for i in range(1, len(list_)):
        new_value = list_[i]
        j = i
        while j > 0 and list_[j - 1] > new_value:
            list_[j] = list_[j - 1]
            j -= 1
        list_[j] = new_value
    return list_

my_list = [3, 4, 1, 9, 2, 4, 3, 7, 8, 0, 3, 5, 1]
print(insertion_sort(my_list))
