class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        needle_len = len(needle)
        i = 0
        
        if needle_len == 0:
            return 0
        
        while True:
            
            if i <= (len(haystack) - needle_len):
                if haystack[i:(i+needle_len)] == needle:
                    return i

                else:
                    i += 1
            
            else:
                return -1