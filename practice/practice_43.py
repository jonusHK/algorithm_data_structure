def solution(target, typed):
    j = 0
    for i in range(len(target)):

        if j >= len(typed):
            return False

        if target[i] == typed[j]:
            j += 1
            continue

        while j < len(typed) - 1:
            j += 1

            if target[i] == typed[j]:
                break

            if target[i-1] != typed[j]:
                return False

    for s in typed[j:]:
        if s != target[-1]:
            return False

    return True


if __name__ == "__main__":
    target = "bucketplace"
    typed = "buckeetplace"
    print(solution(target, typed))
