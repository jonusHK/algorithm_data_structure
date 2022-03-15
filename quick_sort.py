import random


def quick_sort(li: list):
    if len(li) <= 1:
        return li

    pivot = li[0]

    left, right = [], []
    for v in li[1:]:
        if v < pivot:
            left.append(v)
        else:
            right.append(v)

    return quick_sort(left) + [pivot] + quick_sort(right)


data_list = random.sample(range(100), 10)
print(quick_sort(data_list))
