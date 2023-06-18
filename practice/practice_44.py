def solution(num):
    num = str(num)
    n = len(num)

    for i in range(n // 2):
        if num[i] != num[n-i-1]:
            return False

    return True


if __name__ == "__main__":
    num = 2144414411414
    print(solution(num))
