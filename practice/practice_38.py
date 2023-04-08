def solution(inputs, pattern):
    result = []
    for input in inputs:
        ptr = 0
        is_break = False
        for s in input:
            if s.isupper() and (ptr == len(pattern) or pattern[ptr] != s):
                is_break = True
                break

            if ptr < len(pattern) and s == pattern[ptr]:
                ptr += 1

        result.append(not is_break and ptr == len(pattern))

    return result


if __name__ == "__main__":
    inputs = ["apPle", "Apple", "AppLE"]
    pattern = "ALE"
    print(solution(inputs, pattern))
