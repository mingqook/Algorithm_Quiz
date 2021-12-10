class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        for word in words:
            test = True
            for char in list(word):
                if list(chars).count(char) < list(word).count(char):
                    test = False
                    
            if test:
                result +=len(word)
                
        return result