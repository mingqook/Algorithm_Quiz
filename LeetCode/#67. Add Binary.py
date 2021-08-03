class Solution:
    def addBinary(self, a: str, b: str) -> str:

        def make_binary_str(s):
            temp_list = []
            for i in range(len(s)):
                if s[i] == '2':
                    temp_list.insert(i,'10' + '0' * (len(s) - i - 1))
                else:
                    temp_list.insert(i, s[i] + '0' * (len(s) - i - 1))
            
            temp_result = 0
            for y in temp_list:
                temp_result += int(y)
                
            return str(temp_result)
        
                
        a_int = int(a)
        b_int = int(b)
        add_int = a_int + b_int
        add_str = str(add_int)
        
        result = make_binary_str(add_str)
        
        while '2' in result:
            result = make_binary_str(result)
        
            
        return result