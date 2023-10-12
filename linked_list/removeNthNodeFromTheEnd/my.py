# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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


