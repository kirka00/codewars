def alphabet_position(text):
    d = {l: i + 1 for i, l in enumerate('abcdefghijklmnopqrstuvwxyz')}
    answer = ''
    string_ = [char for char in text.lower()]
    for i in string_:
        if i in r" !@#.</-,'":
            pass
        else:
            answer += str(d[i]) + " "
    return answer.strip()
