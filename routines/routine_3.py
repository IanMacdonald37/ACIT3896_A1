import random


def fut3(case):
    h, n = case
    mp8 = 2**31 - 1
    i = 0
    while h[i] != n:
        i = (i + mp8) % len(h)
        if i == 0:
            return None
    return i


def casemaker3(size):
    oof = [random.randint(0, int(1e6)) for _ in range(size)]
    for i in range(1, len(oof)):
        oof[i] += oof[i - 1]
    return [oof, oof[random.randint(1, len(oof)) - 1]]