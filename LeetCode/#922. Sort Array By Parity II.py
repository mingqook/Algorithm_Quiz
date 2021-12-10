class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        temp = [-1] * len(nums)
        odd_list = [x for x in range(len(nums)) if x % 2 == 1]
        even_list = [x for x in range(len(nums)) if x %2 == 0]
        
        for i, x in enumerate(nums):
            
            if (i % 2) == (x % 2) and (i %2 ==0):
                temp[even_list.pop()] = x
                
            elif (i % 2) == (x % 2) and (i %2 ==1):
                temp[odd_list.pop()] = x
                
            elif (i % 2) != (x % 2) and (i %2 ==0):
                temp[odd_list.pop()] = x
            
            else:
                temp[even_list.pop()] = x

        return temp