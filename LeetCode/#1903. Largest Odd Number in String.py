class Solution:
    def largestOddNumber(self, num: str) -> str:
        temp = list(num)
        i = len(num)
        while True:
            if int(temp.pop()) % 2 == 1:
                return num[:i]
            else:
                if len(temp) == 0:
                    return ""
                else:
                    i -= 1