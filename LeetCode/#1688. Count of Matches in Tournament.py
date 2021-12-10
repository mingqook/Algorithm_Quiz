class Solution:
    def numberOfMatches(self, n: int) -> int:
        teams = n
        counts = 0
        while teams > 1:
            if teams % 2 == 0:
                counts += (teams / 2)
                teams /= 2
            else:
                counts += ((teams - 1) / 2)
                teams = ((teams - 1) / 2) + 1
        
        return int(counts)