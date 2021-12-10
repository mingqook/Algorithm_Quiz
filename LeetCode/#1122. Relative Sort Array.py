class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        result_list = []
        for x in arr2:
            while arr1.count(x) != 0:
                result_list.append(arr1.pop(arr1.index(x)))
        
        for i in list(sorted(arr1)):
            result_list.append(i)
            
        return result_list