class Solution:
    def maximumTime(self, time: str) -> str:

        result = [x for x in time]
        
        temp_list = time.split(":")
        
        for i,x in enumerate(temp_list[0]):
            if x == '?':
                if i == 0:
                    if result[1] != '?' and int(result[1]) >= 4:
                        result[i] = '1'
                    else:
                        result[i] = '2'
                    
                elif i == 1:
                    if result[0] == '2':
                        result[i] = '3'
                    else:
                        result[i] = '9'
                        
        for i, x in enumerate(temp_list[1]):
            if x == '?':
                if i == 0:
                    result[i+3] = '5'
                else:
                    result[i+3] = '9'

                    
        return ''.join(result)