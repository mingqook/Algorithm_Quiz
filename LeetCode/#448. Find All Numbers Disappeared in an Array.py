class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp_set = set([i for i in range(1, len(nums)+ 1)])
        
        return list(temp_set - set(nums))