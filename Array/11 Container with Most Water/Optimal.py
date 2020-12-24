def maxArea(self, height):
    if not height or len(height) == 1:
        return 0

    start = 0
    end = len(height) - 1
    maximumVol = 0

    while start != end:
        currentVol = min(height[start], height[end]) * (end - start)
        maximumVol = max(maximumVol, currentVol)

        if height[start] < height[end]:
            temp = height[start]
            while height[start] <= temp and start != end:
                start = start + 1
        else:
            temp = height[end]
            while height[end] <= temp and start != end:
                end = end - 1

    return maximumVol