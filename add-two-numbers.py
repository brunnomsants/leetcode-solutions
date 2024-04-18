class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode()
        currpnt = dum
        carryv = 0
        while l1 or l2 or carryv:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carryv
            carryv = val//10
            val = val%10
            currpnt.next = ListNode(val)
            currpnt = currpnt.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dum.next
            


        