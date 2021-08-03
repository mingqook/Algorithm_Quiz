class Solution:
    def reverse(self, x: int) -> int:
        temp = ''
        if x > 0:
            x_str_list = list(str(x))
            x_reverse = x_str_list[::-1]
            for i in range(len(x_reverse)):
                temp += x_reverse[i]

            result = int(temp)

        elif x < 0:
            x_str_list = list(str(x))
            x_reverse = x_str_list[::-1]
            for i in range(len(x_reverse)-1):
                temp += x_reverse[i]

            result = int(x_reverse[len(x_reverse)-1] + temp)
        else:
            result = 0
            
        if result >= - (2**31) and result <= (2**31 -1):
            return result
        else:
            return 0