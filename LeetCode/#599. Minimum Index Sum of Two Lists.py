class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        temp = len(list1) + len(list2)
        for i in range(len(list1)):
            a = list1[i]
            if a in list2:
                j = list2.index(a)
                if (i+j) < temp:
                    result_temp = []
                    temp = (i+j)
                    result_temp.append(a)
                    
                elif (i+j) == temp:
                    result_temp.append(a)
                
        return result_temp