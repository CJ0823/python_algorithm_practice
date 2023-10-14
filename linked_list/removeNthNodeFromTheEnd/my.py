# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 1
        i = head
        while i.next:
            sz += 1
            i = i.next
        if sz == 1:
            return

        h, before = head, head
        from_start = sz - n + 1
        while from_start > 1:
            before = h
            h = h.next
            from_start -= 1
        if before.next:
            if h.next:
                before.next = h.next
            else:
                before.next = None
        return head

class Solution2:
    class Solution:
        def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            if head.next is None:
                return None

            vals = []
            while head is not None:
                vals.append(head.val)
                head = head.next

            target_idx = len(vals) - n
            s = ListNode(val=None)
            new_head = s
            for idx in range(0, len(vals)):
                if idx == target_idx:
                    continue
                else:
                    if s.val is None:
                        s = ListNode(val=vals[idx])
                        new_head = s
                    else:
                        s.next = ListNode(val=vals[idx])
                        s = s.next
            return new_head
Solution2().removeNthFromEnd(head=head, n=2)