class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        result = 0
        for i in range(len(word)):
            if len(word) - i - 1 >= 4:
                for j in range(len(word) - i):
                    if (i+j+5) > (len(word)):
                        pass
                    else:
                        if set(word[i:(i+j+5)]) == set('aeiou'):
                            result +=1

        return result