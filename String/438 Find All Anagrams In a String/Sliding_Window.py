def findAnagrams(self, s, p):
    p_count = [0] * 26
    window_count = [0] * 26
    results = []

    if len(p) > len(s):
        return []

    # gets count of each letter in string p
    for letter in p:
        p_count[ord(letter) - ord('a')] += 1

    for i in range(len(s)):
        # check for out of bounds at end of array
        if i == (len(s) - len(p) + 1):
            break

        if i == 0:
            for j in range(len(p)):
                window_count[ord(s[j]) - ord('a')] += 1
            if p_count == window_count:
                results.append(0)
            continue

        window_count[ord(s[i - 1]) - ord('a')] -= 1
        window_count[ord(s[i + len(p) - 1]) - ord('a')] += 1

        if p_count == window_count:
            results.append(i)

    return results