class Solution:
    def romanToInt(self, s: str) -> int:
        s_dict = {'I' : 1,'V' : 5,'X' : 10,'L' : 50,
                  'C' : 100, 'D' : 500, 'M' : 1000}
        result = 0
        for i in range(0, len(s)-1):
            if s_dict[s[i]] < s_dict[s[i+1]]:
                result = result - s_dict[s[i]]
            else:
                result = result + s_dict[s[i]]
                
        result = result + s_dict[s[len(s)-1]]
        
        return result