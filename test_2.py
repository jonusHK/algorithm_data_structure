def solution(S):
    stack = []
    operations = S.split()
    try:
        for op in operations:
            if op.isdigit() == True:
                stack.append(int(op))
            elif op == 'POP':
                stack.pop()
            elif op == 'DUP' :
                top = stack.pop()
                stack.append(top)
                stack.append(top)
            elif op == '+':
                top_1 = stack.pop()
                top_2 = stack.pop()
                stack.append(top_1 + top_2)
            # '-'인 경우
            else:
                top_1 = stack.pop()
                top_2 = stack.pop()
                stack.append(top_1 - top_2)
        return stack.pop()
    except IndexError as e:
        raise e
    
print(solution('4 5 6 - 7 +'))