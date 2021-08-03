class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_reverse_list = list(str(x))[::-1]
            temp = ''
            for i in range(len(x_reverse_list)):
                temp += x_reverse_list[i]
            
            if temp == str(x):
                return True
            else: 
                return False