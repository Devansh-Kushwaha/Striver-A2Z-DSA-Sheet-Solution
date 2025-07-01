# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        heap=[]
        count=0
        for i in lists:
            if i:
                heapq.heappush(heap,(i.val,count,i))
                count+=1
        if heap:
            cur=heapq.heappop(heap)
            ans=ListNode(cur[0])
            nex=cur[2].next
            root=ans
            if nex:
                heapq.heappush(heap,(nex.val,count,nex))
                count+=1
        else:
            return None

        while heap:
            cur=heapq.heappop(heap)
            temp=ListNode(cur[0])
            ans.next=temp
            ans=ans.next
            nex=cur[2].next
            if nex:
                heapq.heappush(heap,(nex.val,count,nex))
                count+=1

        return root
        
