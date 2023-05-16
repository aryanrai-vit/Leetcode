# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead=ListNode()
        dummyHead.next=head
        curr=dummyHead

        while curr.next and curr.next.next:
            temp1=curr.next
            temp2=curr.next.next
            curr.next,temp2.next,temp1.next=temp2,temp1,temp2.next
            curr=temp1
        return dummyHead.next