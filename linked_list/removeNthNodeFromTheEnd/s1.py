from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        # Advance first pointer so that the gap between first and second is n+1 nodes apart
        for i in range(n + 1):
            first = first.next

        # Move first to the end, maintaining the gap
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        return dummy.next