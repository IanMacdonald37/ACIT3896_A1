import random

def fut1(case):
    fut1_2(case, 0, len(case) - 1)
    return case


def fut1_2(case, s, t):
    if t < s:
        return
    if case[s] > case[t]:
        case[s], case[t] = case[t], case[s]
    if t > s + 1:
        q = (t - s + 1) // 3
        fut1_2(case, s, t - q)
        fut1_2(case, s + q, t)
        fut1_2(case, s, t - q)


def casemaker1(size):
    return [random.randint(0, 10**9) for _ in range(size)]

