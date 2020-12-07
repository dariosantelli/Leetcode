def coinChange(self, coins, amount):
    results = []
    coins.sort(reverse=True)
    self.helper(coins, amount, results, 0)
    if not results:
        return -1
    else:
        return results[0]


def helper(self, coins, amount, results, number):
    if amount < 0:
        return
    elif amount == 0:
        results.append(number)
    else:
        for i in range(len(coins)):
            self.helper(coins, amount - coins[i], results, number + 1)