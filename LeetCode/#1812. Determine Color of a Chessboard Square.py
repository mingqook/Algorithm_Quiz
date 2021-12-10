class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        row = int(coordinates[1])
        col = ord(coordinates[0]) - 96
        
        if col % 2 == 0:
            if row % 2 ==0:
                return False
            else:
                return True
        else:
            if row %2 == 1:
                return False
            else:
                return True