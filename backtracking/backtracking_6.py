"""
백준 - N-Queen (3344) -> 백트래킹 알고리즘 사용하면 시간 및 메모리 초과
"""

n = int(input())
array = [[0 for _ in range(n)] for _ in range(n)]
checked_row = [0 for _ in range(n)]


def is_valid(x: int, y: int):
    if next((v for v in array[x] if v == 1), None):
        return False

    if next((a for a in array if a[y] == 1), None):
        return False

    i = 1
    while (
        (0 <= x - i < n and 0 <= y + i < n)
        or (0 <= x + i < n and 0 <= y + i < n)
        or (0 <= x + i < n and 0 <= y - i < n)
        or (0 <= x - i < n and 0 <= y - i < n)
    ):
        for coords in ((x - i, y + i), (x + i, y + i), (x + i, y - i), (x - i, y - i)):
            try:
                if 0 <= coords[0] and 0 <= coords[1] and array[coords[0]][coords[1]] == 1:
                    return False
            except IndexError:
                pass

        i += 1

    return True


def dst(row: int):
    if row == n:
        return

    checked_row[row] = 1
    for col in range(n):
        if is_valid(row, col):
            array[row][col] = 1
            dst(row + 1)
            if checked_row[-1] != 1:
                array[row][col] = 0
            else:
                return

    checked_row[row] = 0


dst(0)

for a in array:
    for i in range(n):
        if a[i] == 1:
            print(i + 1)
            break
