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
    rst = set()
    for v in range(1, len(numbers) + 1):
        rst |= set(map(convert_to_number, permutations(list(numbers), v)))

    for num in rst:
        if checker(num):
            answer += 1

    return answer

print(solution("17"))



