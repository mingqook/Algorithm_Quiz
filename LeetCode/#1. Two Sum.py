class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = nums[i]
            for j in range((i+1), len(nums),1):
                temp2 = nums[j]
 
                if temp + temp2 != target:
                    pass
                else:
                    return [i, j]