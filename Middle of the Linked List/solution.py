# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        slow=head
        fast=head
        while fast:
            fast=fast.next
            slow=slow.next
            if fast:
                fast=fast.next
                if not fast:
                    return slow
            if not fast.next:
                return slow
            

        return slow
        
