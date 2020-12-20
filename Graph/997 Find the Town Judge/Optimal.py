def findJudge(self, N, trust):
    out = [0] * (N + 1)
    inn = [0] * (N + 1)

    for pair in trust:
        out[pair[0]] += 1
        inn[pair[1]] += 1

    for i in range(N):
        if out[i + 1] == 0 and inn[i + 1] == N - 1:
            return i + 1

    return -1 