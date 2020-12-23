def merge(self, intervals):
    results = []
    start = []
    end = []
    stack = []
    temp = [0, 0]

    startPtr = 0
    endPtr = 0

    for interval in intervals:
        start.append(interval[0])
        end.append(interval[1])

    start = sorted(start)
    end = sorted(end)

    while startPtr != len(intervals) or endPtr != len(intervals):
        if startPtr != len(intervals) and start[startPtr] <= end[endPtr]:
            if not stack:
                temp[0] = start[startPtr]
            stack.append(start[startPtr])
            startPtr += 1
        else:
            stack.pop()
            temp[1] = end[endPtr]

            if not stack:
                results.append(copy.copy(temp))
            endPtr += 1

    return results