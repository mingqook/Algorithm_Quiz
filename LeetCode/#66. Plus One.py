class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        temp = ''
        for x in digits:
            temp += str(x)
            
        temp = int(temp)
        temp += 1
        
        result = []
        for y in str(temp):
            result.append(int(y))
            
        return result