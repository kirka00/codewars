def printer_error(s):
    count = 0
    res = ['n', 'o', 'p', 'r', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in s:
        if i in res:
            count += 1
    return f'{count}/{len(s)}'
