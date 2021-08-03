class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        key = edges.pop()
        
        key_1 = key.pop()
        
        if key_1 in edges.pop():
            return key_1
        else:
            return key.pop()