class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr_sort = sorted(arr)
        
        test = [x[0] - x[1] for x in zip(arr_sort[:-1], arr_sort[1:])]
        if len(set(test)) == 1:
            return True
        else:
            return False