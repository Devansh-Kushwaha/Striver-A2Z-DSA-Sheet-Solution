# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        stack=[]
        prehead=head
        c=0
        ans=None
        while head:
            stack.append(head)
            head=head.next
            if len(stack)==k:
                if c==0:
                    c=1
                    ans=stack[-1]
                while stack:
                    x=stack.pop()
                    prehead.next=x
                    prehead=prehead.next
        if stack:
            prehead.next=stack[0]
        else:
            prehead.next=None
        return ans
