def countBits(self, num):
    results = [-1] * (num + 1)

    for i in range(len(results)):
        index = i
        count = 0
        while index != 0:
            if results[index] != -1:
                count += results[index]
                break
            remainder = index % 2
            index = index // 2
            if remainder == 1:
                count += 1
        results[i] = count

    return results