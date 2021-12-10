class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_num = list(text).count(" ")
        word_num = len(text.split())
        
        if word_num > 1:
            between_num = space_num // (word_num - 1)
            end_num = space_num % (word_num -1)

            result = []
            for i in range(len(text.split())-1):
                result.append(text.split()[i])
                result.append(" " * between_num)

            result.append(text.split()[-1])
            result.append(" " * end_num)
            
            
        
        else:
            result = []
            result.append(text.split()[-1])
            result.append(" " * space_num)
            
        return ''.join(result)
