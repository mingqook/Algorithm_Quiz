class Solution:
    def mySqrt(self, x: int) -> int:
        
        i = 1
        
        while i <= (x / i):
            i += 1
            if i == (x / i):
                return i
            
            
        return (i-1)