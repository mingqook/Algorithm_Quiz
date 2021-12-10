class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ''
        temp = s.split("#")
        for num in temp[:-1]:
            if len(num) > 2:
                for num2 in num[:-2]:
                    result += chr(int(num2) + 96)
                result += chr(int(num[-2:]) + 96)
            else:
                result += chr(int(num) + 96)
        
        if temp[-1] == '':
            return result
        else:
            for num3 in temp[-1]:
                result += chr(int(num3) + 96)
            return result