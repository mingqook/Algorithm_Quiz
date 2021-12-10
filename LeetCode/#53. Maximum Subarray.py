class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        temp = nums[0]
        for num in nums[1:]:
            temp = max(temp, 0) + num
            result = max(temp, result)
            
            
        return result