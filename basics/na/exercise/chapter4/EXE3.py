# pair up smallest value with the largest value, and so on.
# 2n input numbers

from com.na.sort.merge_sort import merge_sort

def pair_numbers(mylist):
    # sort numbers using one of the O(nlogn) algorithm
    sort_numbers(mylist)
    n = (len(mylist))//2

    result_list = [(0, 0)] * n
    for i in range(0, n):
        result_list[i] = (mylist[i], mylist[2 * n - i - 1])

    return result_list


def sort_numbers(_list):
    merge_sort(_list)


testlist = [1, 3, 5, 9]
print(pair_numbers(testlist))