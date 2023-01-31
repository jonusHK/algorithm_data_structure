from typing import List

n, m = map(int, input().split())
name_a, name_b = input().split()

mapping = {
    'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1, 'H': 3, 'I': 1,
    'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2,
    'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1
}

left = name_a[m:] if n > m else name_b[n:]
string = ''
for x, y in zip(name_a, name_b):
    string += (x + y)
string += left

array: List[int] = [mapping[s] for s in string]

for i in range(n + m - 2):
    for j in range(n + m - 1 - i):
        array[j] = (array[j] + array[j+1]) % 10

print(f'{array[0] * 10 + array[1] * 1}%')
