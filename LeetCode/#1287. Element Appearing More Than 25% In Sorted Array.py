class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        set_arr = set(arr)
        for i in set_arr:
            if arr.count(i) > (len(arr) * 0.25):
                return i