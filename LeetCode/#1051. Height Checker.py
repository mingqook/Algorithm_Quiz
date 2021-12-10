class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)
        return sum([x[0] != x[1] for x in zip(heights, exp)])