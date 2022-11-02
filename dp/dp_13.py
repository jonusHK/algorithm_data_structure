"""
백준 - 가장 긴 증가하는 부분 수열 4
"""

n = int(input())
array = list(map(int, input().split()))

count_array, trace_array = [], []
for i in range(n):
    count_array.append(1)
    trace_array.append(i)

max_idx, max_len = 0, 1
for i in range(n):
    for j in range(i):
        if array[i] > array[j] and count_array[j] + 1 > count_array[i]:
            count_array[i] = count_array[j] + 1
            trace_array[i] = j
            if max_len < count_array[i]:
                max_idx = i
                max_len = count_array[i]

print(max_len)
if max_len == 1:
    print(array[max_idx])
else:
    result = [array[max_idx]]
    while max_idx != trace_array[max_idx]:
        max_idx = trace_array[max_idx]
        result.append(array[max_idx])

    for i in range(len(result) - 1, -1, -1):
        print(result[i], end=" ")
