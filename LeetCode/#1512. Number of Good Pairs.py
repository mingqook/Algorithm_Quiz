class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for _ in range(len(nums)):
            temp = nums.pop()
            if temp in nums:
                result += nums.count(temp)
            else:
                pass
            
        return result