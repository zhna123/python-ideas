def quick_sort(list_, left, right):
    index = partition(list_, left, right)
    if left < index - 1:
        quick_sort(list_, left, index - 1)
    if index < right:
        quick_sort(list_, index, right)
    return list_


def partition(list_, left, right):
    i = left
    j = right
    pivot_index = (left + right) // 2
    pivot = list_[pivot_index]

    while i <= j:
        while list_[i] < pivot:
            i += 1
        while list_[j] > pivot:
            j -= 1
        if i <= j:
            tmp = list_[i]
            list_[i] = list_[j]
            list_[j] = tmp
            i += 1
            j -= 1
    return i

my_list = [3, 4, 1, 9, 2, 4, 3, 7, 8, 0, 3, 5, 1]
print(quick_sort(my_list, 0, len(my_list) - 1))
