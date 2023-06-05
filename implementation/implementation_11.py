"""
프로그래머스 - 전화번호 목록
"""


def solution(phone_book):
    mapper = {}
    phone_book.sort()

    for phone in phone_book:
        ptr = 1
        while ptr <= len(phone):
            key = phone[:ptr]
            if mapper.get(key):
                return False

            ptr += 1

        mapper[phone] = 1

    return True


if __name__ == "__main__":
    phone_book = ["12", "123", "1235", "567", "88"]
    print(solution(phone_book))
