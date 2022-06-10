"""
백준 - 암호 만들기
"""

l, c = map(int, input().split())
array = input().split()
array.sort()

m_set = {'a', 'e', 'i', 'o', 'u'}


def validate():
    c_set = {_c for _c in cipher}
    x = c_set & m_set
    y = c_set - m_set
    return len(x) >= 1 and len(y) >= 2


def dfs(current_idx: int):
    global cipher
    if len(cipher) == l:
        if validate():
            print(cipher)
        return

    for i in range(current_idx, c):
        cipher += array[i]
        dfs(i + 1)
        cipher = cipher[:-1]


cipher = ''
dfs(0)
