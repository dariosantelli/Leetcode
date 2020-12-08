def minMeetingRooms(self, intervals):
    if not intervals:
        return 0
    min_val = float("inf")
    max_val = float("-inf")
    result = 0

    # gets maximum and minimum values of all intervals
    for interval in intervals:
        max_val = max(max_val, interval[1])
        min_val = min(min_val, interval[0])

    intervalArray = [0] * (max_val - min_val)

    for i in range(len(intervals)):
        startingIdx = intervals[i][0] - min_val - 1
        count = intervals[i][1] - intervals[i][0]
        for j in range(count):
            intervalArray[startingIdx + j] += 1
            result = max(result, intervalArray[startingIdx + j])

    return result