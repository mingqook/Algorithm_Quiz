class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s_list = s.rstrip().split(" ")
        
        return len(s_list[-1])