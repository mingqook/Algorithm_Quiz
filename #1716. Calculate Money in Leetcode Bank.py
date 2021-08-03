class Solution:
    def totalMoney(self, n: int) -> int:
        
        weeks = n // 7

        remain_day = n%7

        x = list(range(1, 8))
        y = list(range(weeks))
        z = list(range(1, remain_day + 1))
        
        if weeks >=1:

            return sum(x) * weeks + 7 * sum(y)  + sum(z) + len(z) * weeks
        
        else:
            return sum(z)