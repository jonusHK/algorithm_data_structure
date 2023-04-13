"""
프로그래머스 - 표현 가능한 이진트리
"""


def convertBinary(value):
    binary = ''
    while value != 0:
        value, left = divmod(value, 2)
        binary += str(left)

    binary = binary[::-1]

    binary_num = 1
    while binary_num < len(binary):
        binary_num = (binary_num + 1) * 2 - 1

    binary = '0' * (binary_num - len(binary)) + binary

    return binary


def dfs(start, end, binary):
    if start == end:
        return binary[start]

    mid = (start + end) // 2

    left = dfs(start, mid - 1, binary)

    if not left or (binary[mid] == '0' and left == '1'):
        return False

    right = dfs(mid + 1, end, binary)
    if not right or (binary[mid] == '0' and right == '1'):
        return False

    if binary[mid] == '0' and left == '0' and right == '0':
        return '0'

    return '1'


def solution(numbers):
    answer = []
    for num in numbers:
        binary = convertBinary(num)
        if dfs(0, len(binary) - 1, binary):
            answer.append(1)
        else:
            answer.append(0)

    return answer


if __name__ == "__main__":
    numbers = [63, 111, 95]
    print(solution(numbers))
