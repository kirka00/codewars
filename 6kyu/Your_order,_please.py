def order(sentence):
    res = '1234567890'
    ans = {}
    for i in sentence.split():
        for j in i:
            if j in res:
                ans[j] = i
    sorted_ = sorted(ans.items(), key=lambda x: x)
    return ' '.join([i[1] for i in sorted_])
