def merge_sort(list_):
    if len(list_) <= 1:
        return list_
    first = list_[0:len(list_)//2]
    second = list_[len(list_)//2:len(list_)]

    # print(first)
    # print(second)

    merge_sort(first)
    merge_sort(second)

    merge(first, second, list_)

    return list_


def merge(first, second, merged):
    first_i = 0
    second_i = 0
    merged_i = 0

    while first_i < len(first) and second_i < len(second):
        if first[first_i] < second[second_i]:
            merged[merged_i] = first[first_i]
            first_i += 1
        else:
            merged[merged_i] = second[second_i]
            second_i += 1
        merged_i += 1

    while first_i < len(first):
        merged[merged_i] = first[first_i]
        merged_i += 1
        first_i += 1
    while second_i < len(second):
        merged[merged_i] = second[second_i]
        merged_i += 1
        second_i += 1

my_list = [3, 4, 1, 9, 2, 4, 3, 7, 8, 0, 3, 5, 1]
print(merge_sort(my_list))
# my_list = [1]
# print(merge_sort(my_list))

