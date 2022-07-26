"""
백준 - 단어 뒤집기 2
"""

sentence = input()
reversed_sentence = ''
target = ''
is_tag = False
for s in sentence:
    if is_tag:
        reversed_sentence += s
        if s == '>':
            is_tag = False
    else:
        if s == '<':
            if target:
                reversed_sentence += target[::-1]
                target = ''
            is_tag = True
            reversed_sentence += s
        else:
            if s == ' ':
                reversed_sentence += target[::-1] + s
                target = ''
            else:
                target += s

if target:
    reversed_sentence += target[::-1]

print(reversed_sentence)
