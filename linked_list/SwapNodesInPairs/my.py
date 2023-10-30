# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(f"val = {self.val}, next = {self.next.val}")
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        ans = ListNode(val=0, next=head.next)
        while head and head.next:
            dummy = head.next
            head.next = head.next.next
            dummy.next = head
            head = dummy.next.next
            if head:
                dummy.next.next = head.next
        return ans.next

head = ListNode()
dummy = head
for i in range(1, 5):
    n = ListNode(val=i)
    head.next = n
    head = head.next

print(Solution().swapPairs(dummy.next))