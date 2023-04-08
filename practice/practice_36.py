def solution(numbers):
    numbers_str = ''.join(list(map(str, numbers)))
    return [int(s) for s in str(int(numbers_str) + 1)]


if __name__ == "__main__":
    numbers = [2, 2, 0, 3]
    print(solution(numbers))
