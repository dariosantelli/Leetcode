def climbStairs(self, n):
    diction = dict()
    diction[1] = 1
    diction[2] = 2
    self.helper(n, diction)
    return diction[n]


def helper(self, n, diction):
    if n in diction:
        return diction[n]
    else:
        diction[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)