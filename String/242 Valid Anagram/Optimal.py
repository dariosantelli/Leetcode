def isAnagram(self, s, t):
    if len(t) != len(s):
        return False

    if not t and not s:
        return True

    count = [0] * 26

    for i in range(len(t)):
        current = ord(t[i]) - ord('a')
        count[current] += 1

    for i in range(len(s)):
        current = ord(s[i]) - ord('a')
        count[current] -= 1

    for i in range(len(count)):
        if count[i] != 0:
            return False

    return True