def solution(s):
    open_str = '({['
    close_str = ')}]'
    count = [0, 0, 0]

    for sign in s:
        for i in range(3):
            if sign == open_str[i]:
                count[i] += 1
            if sign == close_str[i]:
                count[i] -= 1
            if count[i] < 0:
                return False

    return not any(count)


if __name__ == "__main__":
    s = "([]){}"
    print(solution(s))
