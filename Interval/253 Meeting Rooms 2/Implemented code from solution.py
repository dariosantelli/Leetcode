def minMeetingRooms(self, intervals):
    if not intervals:
        return 0
    start_times = []
    end_times = []

    for interval in intervals:
        start_times.append(interval[0])
        end_times.append(interval[1])

    start_times = sorted(start_times)
    end_times = sorted(end_times)

    start_ptr = 0
    end_ptr = 0

    confRooms = 0
    maxConfRooms = 0

    while start_ptr != len(start_times):
        if start_times[start_ptr] < end_times[end_ptr]:
            confRooms += 1
            start_ptr += 1
        else:
            confRooms -= 1
            end_ptr += 1

        maxConfRooms = max(confRooms, maxConfRooms)

    return maxConfRooms