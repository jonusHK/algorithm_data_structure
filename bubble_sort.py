def bubble_sort(array: list):
    for idx in range(len(array) - 1):
        changed = False
        for idx2 in range(len(array) - idx - 1):
            if array[idx2] > array[idx2 + 1]:
                array[idx2], array[idx2 + 1] = array[idx2 + 1], array[idx2]
                changed = True

        if changed is False:
            break

    return array


li = [10, 3, 4, 1, 5, 7, 2, 8, 9]
print(bubble_sort(li))
