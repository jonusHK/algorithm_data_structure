import random


def merge(left: list, right: list):
    rst = []
    left_pointer, right_pointer = 0, 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            rst.append(left[left_pointer])
            left_pointer += 1
        else:
            rst.append(right[right_pointer])
            right_pointer += 1

    if left_pointer < len(left):
        rst.extend(left[left_pointer:])
    else:
        rst.extend(right[right_pointer:])

    return rst


def merge_sort(li: list):
    if len(li) <= 1:
        return li

    mid = len(li) // 2
    left, right = li[:mid], li[mid:]

    return merge(merge_sort(left), merge_sort(right))


data_list = random.sample(range(100), 10)
print(merge_sort(data_list))
