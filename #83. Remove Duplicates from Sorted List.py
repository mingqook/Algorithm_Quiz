# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        result = None
        temp_list = []
        
        while head != None:
            
            if (head.val == None):
                break
            
            else:
                if (head.next == None):
                    if head.val in temp_list:
                        break
                    else:
                        temp_list.append(head.val)
                else:
                    now_head_val = head.val
                    next_head = head.next
                    next_head_val = next_head.val

                    if now_head_val != next_head_val:
                        temp_list.append(now_head_val)
                
            head = head.next
                   
        while True:
            if len(temp_list) == 0:
                break
            
            else:
                result = ListNode(temp_list.pop(), result)
                
        return result