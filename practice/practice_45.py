def solution(s):
    cnt = {}

    for i in s:
        if i not in cnt:
            cnt[i] = 0

        cnt[i] += 1

    string = ''
    for v, c in sorted(cnt.items(), key=lambda x: (-x[1], x[0])):
        string += v * c

    return string


if __name__ == "__main__":
    # 빈도수 내림 차순 정렬
    # 단, 빈도수 동일 -> 사전순 정렬
    # 1 <= s 길이 <= 50,000
    s = "bucketplace"
    print(solution(s))
