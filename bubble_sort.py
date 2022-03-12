def bubble_sort(li: list):
    for idx in range(len(li) - 1):
        changed = False
        for idx2 in range(len(li) - idx - 1):
            if li[idx2] > li[idx2 + 1]:
                li[idx2], li[idx2 + 1] = li[idx2 + 1], li[idx2]
                changed = True

        if changed is False:
            break

    return li


li = [10, 3, 4, 1, 5, 7, 2, 8, 9]
print(bubble_sort(li))
