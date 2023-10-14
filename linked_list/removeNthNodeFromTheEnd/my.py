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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return head

        vals = []
        while head.next is not None:
            vals.append(head.val)
            head = head.next

        target_idx = len(vals) - n
        new_head = ListNode(val=None)
        start = new_head
        for idx in range(0, len(vals)):
            if idx == target_idx:
                continue
            else:
                if new_head.val is None:
                    new_head = ListNode(val=vals[idx])
                    start = new_head
                else:
                    new_head.next = ListNode(val=vals[idx])
                    new_head = new_head.next
        return start


