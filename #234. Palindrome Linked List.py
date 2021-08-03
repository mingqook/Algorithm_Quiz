# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        result_list = []
        
        while True:
            
            if head == None:
                break
            
            result_list.append(head.val)
            head = head.next
            
        return result_list == result_list[::-1]