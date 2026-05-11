class DoublyLinkedList:
    def __init__(self, val, prev=None, next = None):
        self.val = val
        self.next = next
        self.prev = prev
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        head = DoublyLinkedList(tokens[0])
        curr = head

        for i in range(1, len(tokens)):
            curr.next = DoublyLinkedList(tokens[i], prev=curr)
            curr = curr.next

        while head is not None:
            if head.val in '+-*/':
                a = int(head.prev.prev.val)
                b = int(head.prev.val)
                if head.val == '+':
                    res = a + b
                elif head.val == '-':
                    res = a - b            
                elif head.val == '*':
                    res = a * b
                else:
                    res = int(a/b)

                head.val = str(res)
                head.prev = head.prev.prev.prev
                if head.prev is not None:
                    head.prev.next = head
                    
            ans = int(head.val)
            head  = head.next


        return ans

        

        