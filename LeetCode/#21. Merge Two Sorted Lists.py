# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = None
        temp_list = []
        
        while True:
            if (l1 != None) and (l2 != None):
                if l1.val > l2.val:
                    temp_list.append(l2.val)
                    l2 = l2.next
                else:
                    temp_list.append(l1.val)
                    l1 = l1.next
            elif (l1 == None) and (l2 != None):
                while l2 != None:
                    temp_list.append(l2.val)
                    l2 = l2.next
            elif (l1 != None) and (l2 == None):
                while l1 != None:
                    temp_list.append(l1.val)
                    l1 = l1.next
            else:
                break
                
        while True:
        
            if len(temp_list) == 0:
                break
            else:
                result = ListNode(temp_list.pop(), result)
            
        return result