# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head
        l= []
        while curr is not None:
            l.append(curr.val)
            curr = curr.next
        head =ListNode(l[-1])
        curr = head
        print(curr.val)
        i = len(l)-1
        while i>0:
            curr.next = ListNode(l[i-1])
            curr = curr.next  
            i-=1
        return head

        
        