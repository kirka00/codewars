def solution(s):
    answer = []
    i, j = 0, 2
    while i <= len(s):
        answer.append(str(s[i:j]))
        i += 2
        j += 2
    if len(s) % 2 != 0:
        del answer[-1]
        answer.append(f'{s[-1]}_')
    else:
        del answer[-1]
    return answer
