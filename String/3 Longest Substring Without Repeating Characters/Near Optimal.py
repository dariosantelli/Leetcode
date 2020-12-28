def lengthOfLongestSubstring(self, s):
    if not s:
        return 0

    if len(s) == 1:
        return 1

    count = set()
    longestLen = 1

    L = 0
    R = 1

    count.add(s[L])

    while True:
        if R == len(s):
            break

        if s[R] in count:
            while s[R] in count:
                count.remove(s[L])
                L += 1
        else:
            count.add(s[R])
            longestLen = max(longestLen, (R - L) + 1)
            R += 1

    return longestLen