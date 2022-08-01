import collections


def count(string):
    ans = collections.defaultdict(int)
    for c in string:
        ans[c] += 1
    if ans:
        return dict(ans)
    else:
        return {}
