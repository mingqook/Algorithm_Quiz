class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        
        step1, step2 = 1, 2
        while n > 2:
            
            result = step1 + step2
            
            step2, step1 = result, step2
            
            n -= 1
            
        return result