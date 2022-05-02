class Solution:
    def maxSubArray(nums: list[int]) -> int:
        max_val = 0
        for i in range(len(nums)):
            for j in range(len(nums)-i):
                j = j + i + 1

                subarray_sum = sum(nums[i:j+1])
                print(nums[i:j], " = ", subarray_sum)

                if subarray_sum > max_val:
                    max_val = subarray_sum
        
        return max_val


Solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])