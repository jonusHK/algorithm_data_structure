from itertools import permutations

def convert_to_number(li):
    return int(''.join(li))

def checker(num):
    if num < 2:
        return False
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

def solution(numbers):
    answer = 0
    length = len(numbers)
    li = []
    for v in numbers:
        li.append(v)
    rst = set()
    for v in range(1, length + 1):
        converted = list(map(convert_to_number, list(permutations(li, v))))
        for c in converted:
            rst.add(c)
    print('rst --- ', rst)
    for num in rst:
        if checker(num):
            answer += 1

    return answer

print(solution("17"))