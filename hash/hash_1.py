import hashlib


def solution():
    keyword = input()
    result = hashlib.sha256(keyword.encode())
    return result.hexdigest()


print(solution())
