# select min element
def selection_sort(list_):
    length = len(list_)
    for i in range(0, length - 1):
        min_index = i
        for j in range(i + 1, length):
            if list_[j] < list_[min_index]:
                min_index = j
        if min_index != i:
            tmp = list_[i]
            list_[i] = list_[min_index]
            list_[min_index] = tmp
    return list_

my_list = [3, 4, 1, 9, 2, 4, 3, 7, 8, 0, 3, 5, 1]
print(selection_sort(my_list))