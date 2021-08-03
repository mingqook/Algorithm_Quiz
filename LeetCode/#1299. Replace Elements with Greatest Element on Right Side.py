class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result_list = []
        
        if len(arr) > 1:
        
            for i in range(len(arr)-1):
                arr.pop(0)
                result_list.append(max(arr))
                
        result_list.append(-1)
        
        return result_list