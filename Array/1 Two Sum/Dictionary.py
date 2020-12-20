def twoSum(self, nums, target):
    checker = dict()

    for i in range(len(nums)):
        if nums[i] in checker:
            if nums[i] * 2 == target:
                return [i, checker[nums[i]]]
            continue
        checker[nums[i]] = i

    for i in range(len(nums)):
        remainder = target - nums[i]
        if remainder == target // 2:
            continue
        if remainder in checker:
            return [i, checker[remainder]]