def majorityElement(self, nums):
    N = len(nums) // 2 + 1
    print(N)
    if len(nums) == 1:
        return nums[0]
    count = dict()
    for i in range(len(nums)):
        if nums[i] in count:
            count[nums[i]] += 1
            if count[nums[i]] == N:
                return nums[i]
        else:
            count[nums[i]] = 1