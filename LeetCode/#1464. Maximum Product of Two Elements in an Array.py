class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        x = nums.pop(nums.index(max(nums))) - 1
        y = nums.pop(nums.index(max(nums))) - 1
        
        return x*y