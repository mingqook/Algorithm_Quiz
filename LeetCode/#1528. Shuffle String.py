class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp = [(x[0], x[1]) for x in zip(s, indices)]
        return ''.join([key[0] for key in sorted(temp, key = lambda x : x[1])])