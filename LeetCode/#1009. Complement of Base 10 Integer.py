class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return sum([2**i for i in range(len(bin(n)[2:]))]) - n