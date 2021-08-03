class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        start = 0
        
        if len(nums) != 0:
            for j in range(len(nums)):
                if nums[j] != val:
                    nums[start] = nums[j]
                    start += 1

                else:
                    nums[j] = '_'

        return start