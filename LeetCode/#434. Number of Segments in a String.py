class Solution:
    def countSegments(self, s: str) -> int:
        
        result = [x for x in s.strip().split(' ') if x != '']
        
        if result == []:
            return 0
        
        return len(result)