def digital_root(n):
    while len(str(n)) > 1:
        q = 0
        for i in str(n):
            q += int(i)
        n = q
    return n
