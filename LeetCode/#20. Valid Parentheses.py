class Solution:
    def isValid(self, s: str) -> bool:
        
        _dict = {'(' : 1, ')' : 4, '{' : 2, '}' : 5, 
                 '[' : 3, ']' : 6}
        
        start_list = [1,2,3]
        
        s_list = [_dict[x] for x in list(s)]
        
        temp_list = list()
        

        for x in s_list:
            result = False
            if x in start_list:
                temp_list.append(x)
            else:
                if len(temp_list) == 0:
                    break
                else:
                    if (temp_list[-1] + 3) == x:
                        temp_list.pop()
                        if len(temp_list) == 0:
                            result = True
                        else:
                            continue
                    else:
                        break

        return result