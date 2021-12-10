class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for x in set(t):
            if s.count(x) != t.count(x):
                return x