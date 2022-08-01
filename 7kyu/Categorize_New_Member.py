def open_or_senior(data):
    answer = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            answer.append('Senior')
        else:
            answer.append('Open')
    return answer
