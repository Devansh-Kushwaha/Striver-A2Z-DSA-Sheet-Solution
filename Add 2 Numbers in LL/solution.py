class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        head=ListNode()
        temp=head
        while l1 or l2:
            if l1:
                v1=l1.val
            else:
                v1=0
            if l2:
                v2=l2.val
            else:
                v2=0
            s=v1+v2+carry
            carry=s//10
            s=s%10
            temp.val=s
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            if l1 or l2:
                x=ListNode()
                temp.next=x
                temp=temp.next
            else:
                if carry:
                    x=ListNode()
                    temp.next=x
                    temp=temp.next
                    temp.val=carry
                    temp.next=None
                else:
                    temp.next=None
            
        return head
