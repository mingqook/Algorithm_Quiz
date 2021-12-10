class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        left_sum = 0
        right_sum = sum(nums)
        
        
        for i in range(len(nums)):

            if left_sum == right_sum - nums[i]:
                return i
            
            else:
                left_sum = left_sum + nums[i]
                right_sum = right_sum - nums[i]
                
                
        return -1