def findMin(self, nums):
    L = 0
    R = len(nums) - 1
    minimum = float("inf")

    while L <= R:
        mid = ((R - L) // 2) + L

        minimum = min(minimum, nums[mid])

        if nums[mid] > nums[R]:
            L = mid + 1
        else:
            R = mid - 1

    return minimum