class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 1
        for j in range(len(nums)-1):
            if nums[j] == nums[(j+1)]:
                pass
            else:
                nums[i] = nums[(j+1)]
                i += 1
                
        return i 