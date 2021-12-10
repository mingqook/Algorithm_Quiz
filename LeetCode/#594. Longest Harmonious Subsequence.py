class Solution:
    def findLHS(self, nums: List[int]) -> int:
        set_num = set(nums)

        result = 0
        
        for x in set_num:
            if (x+1) in set_num:
                temp = (nums.count(x) + nums.count((x+1)))
                if temp > result:
                    result = temp
                    
        return result