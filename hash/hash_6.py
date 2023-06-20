def solution(numbers, target):
    mapper = {}
    for i in range(len(numbers)):
        mapper[numbers[i]] = i
        other_idx = mapper.get(target-numbers[i], 0)
        if other_idx:
            return sorted([i, other_idx])


if __name__ == "__main__":
    numbers = [2, 5, 1, 8, 9, 2]
    target = 17
    print(solution(numbers, target))
