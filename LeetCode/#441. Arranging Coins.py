class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        temp = [int((2*n) ** (1/2)) -1, int((2*n) ** (1/2))]
        
        for i in range(len(temp)):
            k = temp.pop()
            if k*(k+1) <= 2*n:
                return k